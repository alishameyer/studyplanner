"""US10 – Zeitmangel erkennen (Xhavid).

Plant die offenen Aufgaben auf die verfügbaren Lernzeiten (früheste Frist
zuerst) und meldet Aufgaben, deren Aufwand nicht vollständig eingeplant
werden kann. Das Modul führt keine Dateioperationen aus.

Lernzeiten: Liste mit Dictionaries {"date": "YYYY-MM-DD", "available_minutes": int}.
"""

from datetime import date

from task_overview import format_date, sort_by_deadline

SAMPLE_AVAILABILITY = [
    {"date": "2026-11-06", "available_minutes": 60},
    {"date": "2026-11-07", "available_minutes": 30},
    {"date": "2026-11-09", "available_minutes": 90},
]


def planned_minutes(tasks, availability):
    """Verteilt die Lernzeit auf offene Aufgaben; gibt {Aufgaben-ID: Minuten} zurück."""
    remaining = {entry["date"]: entry["available_minutes"] for entry in availability}
    planned = {}
    for task in sort_by_deadline([t for t in tasks if not t["completed"]]):
        planned[task["id"]] = 0
        for day in sorted(remaining):
            if day > task["deadline"]:
                break
            used = min(remaining[day], task["estimated_minutes"] - planned[task["id"]])
            remaining[day] -= used
            planned[task["id"]] += used
    return planned


def find_shortages(tasks, availability, today=None):
    """Gibt (Aufgabe, fehlende Minuten, überfällig) für Aufgaben mit Engpass zurück."""
    today = (today or date.today()).isoformat()
    planned = planned_minutes(tasks, availability)
    shortages = []
    for task in sort_by_deadline([t for t in tasks if not t["completed"]]):
        missing = task["estimated_minutes"] - planned[task["id"]]
        overdue = task["deadline"] < today
        if missing > 0 or overdue:
            shortages.append((task, missing, overdue))
    return shortages


def show_shortages(tasks, availability, today=None):
    """Gibt die Engpasswarnungen in der Konsole aus."""
    print("\n--- Engpässe ---")
    shortages = find_shortages(tasks, availability, today)
    if not shortages:
        print("Keine Engpässe: Alle offenen Aufgaben sind vollständig eingeplant.")
        return
    for task, missing, overdue in shortages:
        line = (f"  {task['title']} | Frist: {format_date(task['deadline'])} | "
                f"Fehlend: {missing} Min.")
        if overdue:
            line += " | ÜBERFÄLLIG"
        print(line)


if __name__ == "__main__":
    from task_overview import SAMPLE_TASKS

    show_shortages(SAMPLE_TASKS, SAMPLE_AVAILABILITY)
