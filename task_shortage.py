"""US10 – Zeitmangel erkennen (Xhavid).

Verteilt die verfügbaren Lernzeiten auf die offenen Aufgaben
(früheste Frist zuerst) und meldet Aufgaben, deren Aufwand nicht
vollständig eingeplant werden kann.

Lernzeiten: Liste mit Dictionaries
{"date": "YYYY-MM-DD", "available_minutes": int}.
"""

from datetime import date

from task_overview import format_date, sort_by_deadline

SAMPLE_AVAILABILITY = [
    {"date": "2026-11-06", "available_minutes": 60},
    {"date": "2026-11-07", "available_minutes": 30},
    {"date": "2026-11-09", "available_minutes": 90},
]


def get_open_tasks(tasks):
    """Gibt die offenen Aufgaben nach Frist sortiert zurück."""
    open_tasks = []
    for task in tasks:
        if not task["completed"]:
            open_tasks.append(task)
    return sort_by_deadline(open_tasks)


def planned_minutes(tasks, availability):
    """Gibt {Aufgaben-ID: eingeplante Minuten} zurück."""
    # Noch freie Minuten pro Tag
    remaining = {}
    for entry in availability:
        remaining[entry["date"]] = entry["available_minutes"]

    planned = {}
    for task in get_open_tasks(tasks):
        planned[task["id"]] = 0
        for day in sorted(remaining):
            # Tage nach der Frist helfen dieser Aufgabe nicht mehr.
            if day > task["deadline"]:
                break
            still_needed = task["estimated_minutes"] - planned[task["id"]]
            used = min(remaining[day], still_needed)
            remaining[day] = remaining[day] - used
            planned[task["id"]] = planned[task["id"]] + used
    return planned


def find_shortages(tasks, availability, today=None):
    """Gibt (Aufgabe, fehlende Minuten, überfällig) pro Engpass zurück."""
    if today is None:
        today = date.today()
    today_text = str(today)  # z. B. "2026-11-09"

    planned = planned_minutes(tasks, availability)
    shortages = []
    for task in get_open_tasks(tasks):
        missing = task["estimated_minutes"] - planned[task["id"]]
        overdue = task["deadline"] < today_text
        if missing > 0 or overdue:
            shortages.append((task, missing, overdue))
    return shortages


def show_shortages(tasks, availability, today=None):
    """Gibt die Engpasswarnungen in der Konsole aus."""
    print("\n--- Engpässe ---")
    shortages = find_shortages(tasks, availability, today)
    if len(shortages) == 0:
        print("Keine Engpässe: Alle offenen Aufgaben sind vollständig "
              "eingeplant.")
        return

    for shortage in shortages:
        task, missing, overdue = shortage
        line = (f"  {task['title']} | Frist: {format_date(task['deadline'])}"
                f" | Fehlend: {missing} Min.")
        if overdue:
            line = line + " | ÜBERFÄLLIG"
        print(line)


if __name__ == "__main__":
    from task_overview import SAMPLE_TASKS

    show_shortages(SAMPLE_TASKS, SAMPLE_AVAILABILITY)
