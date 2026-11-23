"""US09 – Aufgaben nach Fach filtern (Xhavid).

Zeigt die Fächer nummeriert an und gibt nur die Aufgaben des gewählten
Fachs aus. Die Anzeige übernimmt show_tasks() aus US04.
"""

from logic.task_overview_US04 import show_tasks


def filter_by_subject(tasks, subject):
    """Gibt nur die Aufgaben des gewählten Fachs zurück."""
    subject_tasks = []
    for task in tasks:
        if task["subject"] == subject:
            subject_tasks.append(task)
    return subject_tasks


def show_tasks_by_subject(tasks, subjects):
    """Fach wählen und dessen Aufgaben anzeigen."""
    print("\n--- Aufgaben nach Fach filtern ---")
    if len(subjects) == 0:
        print("Es sind noch keine Fächer erfasst.")
        return

    for number in range(1, len(subjects) + 1):
        print(f"  ({number}) {subjects[number - 1]}")

    try:
        choice = int(input("Auswahl: "))
    except ValueError:
        choice = 0
    if choice < 1 or choice > len(subjects):
        print(f"⚠️ Bitte eine Zahl von 1 bis {len(subjects)} wählen.")
        return

    subject = subjects[choice - 1]
    subject_tasks = filter_by_subject(tasks, subject)
    if len(subject_tasks) == 0:
        print(f"Für das Fach {subject} gibt es keine Aufgaben.")
    else:
        show_tasks(subject_tasks)
