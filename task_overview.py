"""US04 – Aufgaben anzeigen (Xhavid).

Zeigt offene Aufgaben nach aufsteigender Frist und erledigte Aufgaben
getrennt an. Das Modul führt keine Dateioperationen aus; die Aufgaben
werden als Liste von Dictionaries übergeben (siehe README).
"""

from datetime import date

WEEKDAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
            "Freitag", "Samstag", "Sonntag"]

PRIORITIES = {1: "niedrig", 2: "mittel", 3: "hoch"}

# Gemeinsame Beispieldaten, solange Erfassen und Laden noch fehlen.
SAMPLE_TASKS = [
    {"id": 1, "title": "Woche 1", "subject": "Mathematik 1",
     "deadline": "2026-10-14", "estimated_minutes": 90,
     "priority": 3, "completed": False},
    {"id": 2, "title": "Projektarbeit", "subject": "Principales of Management",
     "deadline": "2026-11-20", "estimated_minutes": 180,
     "priority": 3, "completed": False},
    {"id": 3, "title": "Moodelpoints holen", "subject": "Digital Business",
     "deadline": "2026-10-05", "estimated_minutes": 20,
     "priority": 3, "completed": True},
]


def format_date(iso_date):
    """Wandelt 'YYYY-MM-DD' in '05.10.2026 (Montag)' um."""
    day = date.fromisoformat(iso_date)
    return f"{day.strftime('%d.%m.%Y')} ({WEEKDAYS[day.weekday()]})"


def sort_by_deadline(tasks):
    """Sortiert Aufgaben nach aufsteigender Frist, bei gleicher Frist nach ID."""
    return sorted(tasks, key=lambda task: (task["deadline"], task["id"]))


def split_tasks(tasks):
    """Teilt Aufgaben in offene und erledigte, jeweils nach Frist sortiert."""
    open_tasks = [task for task in tasks if not task["completed"]]
    done_tasks = [task for task in tasks if task["completed"]]
    return sort_by_deadline(open_tasks), sort_by_deadline(done_tasks)


def format_task(task):
    """Eine Zeile mit ID, Titel, Fach, Frist, Aufwand und Priorität."""
    priority = PRIORITIES.get(task["priority"], str(task["priority"]))
    return (f"ID {task['id']}: {task['title']} | {task['subject']} | "
            f"Frist: {format_date(task['deadline'])} | "
            f"{task['estimated_minutes']} Min. | Priorität: {priority}")


def show_tasks(tasks):
    """Gibt die Aufgabenübersicht in der Konsole aus."""
    print("\n--- Aufgabenübersicht ---")
    if not tasks:
        print("Es sind noch keine Aufgaben erfasst.")
        return

    open_tasks, done_tasks = split_tasks(tasks)

    print("\nOffene Aufgaben (nach Frist):")
    if open_tasks:
        for task in open_tasks:
            print("  " + format_task(task))
    else:
        print("  Keine offenen Aufgaben.")

    print("\nErledigte Aufgaben:")
    if done_tasks:
        for task in done_tasks:
            print("  " + format_task(task))
    else:
        print("  Keine erledigten Aufgaben.")


if __name__ == "__main__":
    show_tasks(SAMPLE_TASKS)
    show_tasks([])
