"""US04 – Aufgaben anzeigen (Xhavid).

Zeigt offene Aufgaben nach Frist sortiert und erledigte Aufgaben
getrennt an. Eine Aufgabe ist ein Dictionary (siehe README).
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

# Wandelt ein Datum von YYYY-MM-DD in DD.MM.YYYY (Wochentag) um.
def format_date(iso_date):
    year = iso_date[0:4]
    month = iso_date[5:7]
    day = iso_date[8:10]
    weekday = date(int(year), int(month), int(day)).weekday()
    return f"{day}.{month}.{year} ({WEEKDAYS[weekday]})"

    
def sort_by_deadline(tasks):
    """Sortiert Aufgaben nach Frist, bei gleicher Frist nach ID."""
    # Tupel werden zuerst nach der Frist, dann nach der ID sortiert.
    pairs = []
    for task in tasks:
        pairs.append((task["deadline"], task["id"], task))
    pairs.sort()

    sorted_tasks = []
    for pair in pairs:
        sorted_tasks.append(pair[2])
    return sorted_tasks


def split_tasks(tasks):
    """Teilt Aufgaben in offene und erledigte, beide nach Frist sortiert."""
    open_tasks = []
    done_tasks = []
    for task in tasks:
        if task["completed"]:
            done_tasks.append(task)
        else:
            open_tasks.append(task)
    return sort_by_deadline(open_tasks), sort_by_deadline(done_tasks)


def format_task(task):
    """Eine Zeile mit ID, Titel, Fach, Frist, Aufwand und Priorität."""
    priority = PRIORITIES.get(task["priority"], str(task["priority"]))
    deadline = format_date(task["deadline"])
    return (f"ID {task['id']}: {task['title']} | {task['subject']} | "
            f"Frist: {deadline} | {task['estimated_minutes']} Min. | "
            f"Priorität: {priority}")


def print_task_list(tasks, empty_text):
    """Gibt jede Aufgabe auf einer Zeile aus oder einen Hinweis."""
    if len(tasks) == 0:
        print("  " + empty_text)
    for task in tasks:
        print("  " + format_task(task))


def show_tasks(tasks):
    """Gibt die Aufgabenübersicht in der Konsole aus."""
    print("\n--- Aufgabenübersicht ---")
    if len(tasks) == 0:
        print("Es sind noch keine Aufgaben erfasst.")
        return

    open_tasks, done_tasks = split_tasks(tasks)
    print("\nOffene Aufgaben (nach Frist):")
    print_task_list(open_tasks, "Keine offenen Aufgaben.")
    print("\nErledigte Aufgaben:")
    print_task_list(done_tasks, "Keine erledigten Aufgaben.")


def filter_by_subject(tasks, subject):
    """Gibt nur die Aufgaben des gewählten Fachs zurück."""
    subject_tasks = []
    for task in tasks:
        if task["subject"] == subject:
            subject_tasks.append(task)
    return subject_tasks


def show_tasks_by_subject(tasks, subjects):
    """US09: Fach wählen und dessen Aufgaben anzeigen."""
    print("\n--- Aufgaben nach Fach filtern ---")
    if len(subjects) == 0:
        print("Es sind noch keine Fächer erfasst.")
        return

    for number in range(1, len(subjects) + 1):
        print(f"  ({number}) {subjects[number - 1]}")

    choice = input("Auswahl: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(subjects):
        print(f"⚠️ Bitte eine Zahl von 1 bis {len(subjects)} wählen.")
        return

    subject = subjects[int(choice) - 1]
    subject_tasks = filter_by_subject(tasks, subject)
    if len(subject_tasks) == 0:
        print(f"Für das Fach {subject} gibt es keine Aufgaben.")
        return
    show_tasks(subject_tasks)


if __name__ == "__main__":
    show_tasks(SAMPLE_TASKS)
    show_tasks([])
