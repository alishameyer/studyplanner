"""Studyplanner – Hauptmenü.

Die Menünummern entsprechen der Tabelle "Bedienung" im README.
Weitere Optionen werden ergänzt, sobald die User Stories umgesetzt sind.
Bis Speichern und Laden (US11, US12) bereitstehen, arbeitet das Programm
mit den gemeinsamen Beispieldaten.
"""

from task_filter import show_tasks_by_subject
from task_overview import SAMPLE_TASKS, show_tasks
from task_shortage import SAMPLE_AVAILABILITY, show_shortages

SAMPLE_SUBJECTS = ["Grundlagen Programmieren", "Mathematik 1", "Statistik 1",
                   "Principales of Management", "Digital Business"]


def main():
    while True:
        print("\n=== Studyplanner ===")
        print("(4) Aufgaben anzeigen")
        print("(9) Aufgaben nach Fach filtern")
        print("(10) Engpässe anzeigen")
        print("(0) Programm beenden")
        choice = input("Auswahl: ").strip()

        if choice == "4":
            show_tasks(SAMPLE_TASKS)
        elif choice == "9":
            show_tasks_by_subject(SAMPLE_TASKS, SAMPLE_SUBJECTS)
        elif choice == "10":
            show_shortages(SAMPLE_TASKS, SAMPLE_AVAILABILITY)
        elif choice == "0":
            print("Auf Wiedersehen 👋")
            break
        else:
            print("⚠️ Ungültige Auswahl.")


if __name__ == "__main__":
    main()
