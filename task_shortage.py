"""US10 – Zeitmangel erkennen (Xhavid).

Verteilt die verfügbaren Lernzeiten auf die offenen Aufgaben
(früheste Frist zuerst) und meldet Aufgaben, deren Aufwand nicht
vollständig eingeplant werden kann.

Lernzeiten: Liste mit Dictionaries
{"date": "YYYY-MM-DD", "available_minutes": int}.
"""

from datetime import date

from task_overview import format_date, split_tasks

SAMPLE_AVAILABILITY = [
    {"date": "2026-11-06", "available_minutes": 60},
    {"date": "2026-11-07", "available_minutes": 30},
    {"date": "2026-11-09", "available_minutes": 90},
]


def planned_minutes(tasks, availability):
    """Gibt {Aufgaben-ID: eingeplante Minuten} zurück."""
    # Noch freie Minuten pro Tag
    remaining = {}
    for entry in availability:
        remaining[entry["date"]] = entry["available_minutes"]
    days = list(remaining)
    days.sort()

    open_tasks, done_tasks = split_tasks(tasks)
    planned = {}
    for task in open_tasks:
        planned[task["id"]] = 0
        for day in days:
            # Tage nach der Frist helfen dieser Aufgabe nicht mehr.
            if day > task["deadline"]:
                break
            used = min(remaining[day], task["estimated_minutes"] - planned[task["id"]])
            remaining[day] -= used
            planned[task["id"]] += used
    return planned


def find_shortages(tasks, availability, today):
    """Gibt (Aufgabe, fehlende Minuten, überfällig) pro Engpass zurück.

    today ist ein Datum als Text, z. B. "2026-11-09".
    """
    planned = planned_minutes(tasks, availability)
    open_tasks, done_tasks = split_tasks(tasks)
    shortages = []
    for task in open_tasks:
        missing = task["estimated_minutes"] - planned[task["id"]]
        overdue = task["deadline"] < today
        if missing > 0 or overdue:
            shortages.append((task, missing, overdue))
    return shortages


def show_shortages(tasks, availability):
    """Gibt die Engpasswarnungen in der Konsole aus."""
    print("\n--- Engpässe ---")
    shortages = find_shortages(tasks, availability, str(date.today()))
    if len(shortages) == 0:
        print("Keine Engpässe: Alle offenen Aufgaben sind vollständig "
              "eingeplant.")
        return

    for task, missing, overdue in shortages:
        line = (f"  {task['title']} | Frist: {format_date(task['deadline'])}"
                f" | Fehlend: {missing} Min.")
        if overdue:
            line += " | ÜBERFÄLLIG"
        print(line)
