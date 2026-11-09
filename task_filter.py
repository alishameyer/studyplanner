"""US09 – Aufgaben nach Fach filtern (Xhavid).

Zeigt die vorhandenen Fächer nummeriert an und gibt nur die Aufgaben
des gewählten Fachs aus: offene nach Frist, erledigte getrennt.
Die Anzeige übernimmt show_tasks() aus US04.
"""

from task_overview import show_tasks


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
    from main import SAMPLE_SUBJECTS
    from task_overview import SAMPLE_TASKS

    show_tasks_by_subject(SAMPLE_TASKS, SAMPLE_SUBJECTS)
