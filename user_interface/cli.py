"""Benutzereingaben in Fachfunktionen übersetzen, kein JSON-Zugriff."""

from logic.availability import set_availability
from user_interface.display import (
    show_availability, show_progress, show_shortfalls, show_tasks,
)
from logic.capacity import calculate_shortfalls
from logic.tasks import (
    add_subject, add_task, complete_task, find_task,
    update_task,
)

MUTATING_CHOICES = {"1", "2", "3", "5", "7"}
MENU = """
1  Fach erfassen                 2  Aufgabe erfassen
3  Aufgabe bearbeiten            4  Aufgaben anzeigen
5  Aufgabe erledigen             6  Fortschritt anzeigen
7  Lernzeit erfassen             8  Lernzeiten anzeigen
9  Aufgaben nach Fach filtern   10  Zeitmangel erkennen
0  Beenden
"""


def ask_int(prompt, current=None):
    """
    Fängt auch Zeichen ab, bei denen isdigit allein nicht ausreicht.
    """
    text = input(prompt).strip()
    if not text and current is not None:
        return current
    try:
        return int(text)
    except ValueError as error:
        raise ValueError("Bitte eine ganze Zahl eingeben.") from error


def ask_text(prompt, current=None):
    """Leere Eingabe behält beim Bearbeiten den bisherigen Wert."""
    text = input(prompt).strip()
    return current if not text and current is not None else text


def choose_subject(data, current=None):
    """
    Zeigt vorhandene Fächer nummeriert; neue Fächer separat erfassen.
    """
    if not data["subjects"]:
        raise ValueError("Bitte zuerst ein Fach erfassen.")
    for number, name in enumerate(data["subjects"], 1):
        print(f"{number}: {name}")
    if current is not None:
        print(f"Enter behält: {current}")
    text = input("Fachnummer: ").strip()
    if not text and current is not None:
        return current
    try:
        index = int(text) - 1
    except ValueError as error:
        raise ValueError("Ungültige Fachnummer.") from error
    if not 0 <= index < len(data["subjects"]):
        raise ValueError("Ungültige Fachnummer.")
    return data["subjects"][index]


def task_fields(data, task=None):
    """
    Sammelt Felder vollständig, bevor das Fachmodul Daten verändert.
    """
    old = {} if task is None else task
    if task is not None:
        print("Enter behält den bisherigen Wert; aktuelle Aufgabe:")
        print(task)
    return (
        ask_text("Titel: ", old.get("title")),
        choose_subject(data, old.get("subject")),
        ask_text("Frist (YYYY-MM-DD): ", old.get("deadline")),
        ask_int("Aufwand in Minuten: ", old.get("estimated_minutes")),
        ask_int("Priorität (1 niedrig / 2 mittel / 3 hoch): ",
                old.get("priority")),
    )


def handle_change(choice, data):
    """
    Ändert nur den vom Aufrufer bereitgestellten Arbeitsdatenbestand.
    """
    if choice == "1":
        add_subject(data, input("Neuer Fachname: "))
    elif choice == "2":
        if not data["subjects"]:
            raise ValueError("Bitte zuerst ein Fach erfassen.")
        add_task(data, *task_fields(data))
    elif choice == "3":
        task_id = ask_int("Aufgaben-ID: ")
        task = find_task(data, task_id)
        update_task(data, task_id, *task_fields(data, task))
    elif choice == "5":
        complete_task(data, ask_int("Aufgaben-ID: "))
    elif choice == "7":
        day = input("Datum (YYYY-MM-DD): ").strip()
        minutes = ask_int("Verfügbare Minuten (positive ganze Zahl): ")
        set_availability(data, day, minutes)


def handle_view(choice, data):
    """Liefert True für bekannte Anzeigeoptionen, sonst False."""
    if choice == "4":
        show_tasks(data)
    elif choice == "6":
        show_progress(data)
    elif choice == "8":
        show_availability(data)
    elif choice == "9":
        show_tasks(data, choose_subject(data))
    elif choice == "10":
        show_shortfalls(data, calculate_shortfalls(data))
    else:
        return False
    return True
