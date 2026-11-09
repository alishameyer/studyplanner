"""Studyplanner – Hauptmenü.

Die Menünummern entsprechen der Tabelle "Bedienung" im README.
Weitere Optionen werden ergänzt, sobald die User Stories umgesetzt sind.
Bis Speichern und Laden (US11, US12) bereitstehen, arbeitet das Programm
mit den gemeinsamen Beispieldaten.
"""

from task_overview import SAMPLE_TASKS, show_tasks, show_tasks_by_subject
from task_shortage import SAMPLE_AVAILABILITY, show_shortages

SAMPLE_SUBJECTS = ["Grundlagen Programmieren", "Mathematik 1", "Statistik 1",
                   "Principales of Management", "Digital Business"]


def main():
    # Kopien, damit die Beispieldaten selbst unverändert bleiben.
    subjects = SAMPLE_SUBJECTS.copy()
    tasks = []
    for task in SAMPLE_TASKS:
        tasks.append(task.copy())
    availability = []
    for entry in SAMPLE_AVAILABILITY:
        availability.append(entry.copy())

    while True:
        print("\n=== Studyplanner ===")
        print("(4) Aufgaben anzeigen")
        print("(9) Aufgaben nach Fach filtern")
        print("(10) Engpässe anzeigen")
        print("(0) Programm beenden")
        choice = input("Auswahl: ").strip()

        if choice == "4":
            show_tasks(tasks)
        elif choice == "9":
            show_tasks_by_subject(tasks, subjects)
        elif choice == "10":
            show_shortages(tasks, availability)
        elif choice == "0":
            print("Auf Wiedersehen 👋")
            break
        else:
            print("⚠️ Ungültige Auswahl.")


if __name__ == "__main__":
    main()
