"""Aufgaben verwalten: erstellen (US02), bearbeiten (US03) und löschen.

Das Untermenü "Aufgabe" bietet:
(1) Aufgabe erstellen, (2) Aufgabe bearbeiten, (3) Aufgabe löschen, (4) Zurück

Das Modul führt keine Dateioperationen aus. Nach einer erfolgreichen
Änderung wird die übergebene Funktion `save` aufgerufen (z. B. aus main.py).
"""

from datetime import date, datetime

from task_overview import PRIORITIES, format_task


# ---------- Validierung ----------

def parse_title(text):
    title = text.strip()
    if not title:
        raise ValueError("Der Titel darf nicht leer sein.")
    return title


def parse_deadline(text):
    """Liest 'DD-MM-YYYY' ein und gibt das Datum als 'YYYY-MM-DD' zurück."""
    try:
        deadline = datetime.strptime(text.strip(), "%d-%m-%Y").date()
    except ValueError:
        raise ValueError("Ungültiges Datum. Bitte im Format DD-MM-YYYY eingeben.")
    if deadline < date.today():
        raise ValueError("Die Frist darf nicht in der Vergangenheit liegen.")
    return deadline.isoformat()


def to_input_date(iso_date):
    """Wandelt 'YYYY-MM-DD' in die Eingabeform 'DD-MM-YYYY' um."""
    return date.fromisoformat(iso_date).strftime("%d-%m-%Y")


def parse_minutes(text):
    text = text.strip()
    if not text.isdigit() or int(text) <= 0:
        raise ValueError("Der Aufwand muss eine positive ganze Minutenzahl sein.")
    return int(text)


def parse_priority(text):
    text = text.strip()
    if text not in ("1", "2", "3"):
        raise ValueError("Die Priorität muss 1, 2 oder 3 sein.")
    return int(text)


def make_subject_parser(subjects):
    def parse_subject(text):
        text = text.strip()
        if not text.isdigit() or not 1 <= int(text) <= len(subjects):
            raise ValueError(f"Bitte eine Zahl von 1 bis {len(subjects)} wählen.")
        return subjects[int(text) - 1]
    return parse_subject


# ---------- Eingabe ----------

def ask(prompt, parse, current=None):
    """Fragt so lange, bis die Eingabe gültig ist.

    Mit `current` (beim Bearbeiten) behält eine leere Eingabe den alten Wert.
    """
    while True:
        text = input(prompt)
        if current is not None and not text.strip():
            return current
        try:
            return parse(text)
        except ValueError as error:
            print(f"⚠️ {error}")


def show_subjects(subjects):
    for number, subject in enumerate(subjects, start=1):
        print(f"  ({number}) {subject}")


def find_task(tasks, text):
    """Sucht eine Aufgabe über ihre ID; gibt None zurück, wenn sie fehlt."""
    text = text.strip()
    if text.isdigit():
        for task in tasks:
            if task["id"] == int(text):
                return task
    return None


def choose_task(tasks):
    """Zeigt alle Aufgaben mit ihrer ID und fragt nach der gewünschten ID."""
    for task in tasks:
        print("  " + format_task(task))
    return find_task(tasks, input("ID der Aufgabe (Zahl nach 'ID'): "))


def next_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1


# ---------- Aktionen ----------

def create_task(tasks, subjects):
    """Erfasst eine neue offene Aufgabe. Gibt True bei Erfolg zurück."""
    print("\n--- Aufgabe erstellen ---")
    if not subjects:
        print("⚠️ Bitte zuerst ein Fach erfassen.")
        return False

    title = ask("Titel: ", parse_title)
    print("Fach:")
    show_subjects(subjects)
    subject = ask("Auswahl: ", make_subject_parser(subjects))
    deadline = ask("Frist (DD-MM-YYYY): ", parse_deadline)
    minutes = ask("Aufwand in Minuten: ", parse_minutes)
    priority = ask("Priorität (1 = niedrig, 2 = mittel, 3 = hoch): ", parse_priority)

    task = {"id": next_id(tasks), "title": title, "subject": subject,
            "deadline": deadline, "estimated_minutes": minutes,
            "priority": priority, "completed": False}
    tasks.append(task)
    print(f"✅ Aufgabe erstellt: {format_task(task)}")
    return True


def edit_task(tasks, subjects):
    """Bearbeitet eine Aufgabe über ihre ID; ID und Status bleiben erhalten."""
    print("\n--- Aufgabe bearbeiten ---")
    task = choose_task(tasks)
    if task is None:
        print("⚠️ Keine Aufgabe mit dieser ID gefunden.")
        return False

    print(format_task(task))
    print("Leere Eingabe behält den bisherigen Wert.")
    title = ask(f"Titel [{task['title']}]: ", parse_title, task["title"])
    print(f"Fach [{task['subject']}]:")
    show_subjects(subjects)
    subject = ask("Auswahl: ", make_subject_parser(subjects), task["subject"])
    deadline = ask(f"Frist (DD-MM-YYYY) [{to_input_date(task['deadline'])}]: ",
                   parse_deadline, task["deadline"])
    minutes = ask(f"Aufwand in Minuten [{task['estimated_minutes']}]: ",
                  parse_minutes, task["estimated_minutes"])
    priority = ask(f"Priorität [{task['priority']} = {PRIORITIES[task['priority']]}]: ",
                   parse_priority, task["priority"])

    task.update({"title": title, "subject": subject, "deadline": deadline,
                 "estimated_minutes": minutes, "priority": priority})
    print(f"✅ Aufgabe geändert: {format_task(task)}")
    return True


def delete_task(tasks):
    """Löscht eine Aufgabe über ihre ID nach Bestätigung."""
    print("\n--- Aufgabe löschen ---")
    task = choose_task(tasks)
    if task is None:
        print("⚠️ Keine Aufgabe mit dieser ID gefunden.")
        return False

    print(format_task(task))
    if input("Wirklich löschen? (j/n): ").strip().lower() != "j":
        print("Löschen abgebrochen.")
        return False
    tasks.remove(task)
    print("✅ Aufgabe gelöscht.")
    return True


# ---------- Untermenü ----------

def task_menu(tasks, subjects, save=None):
    """Untermenü "Aufgabe". Ruft nach jeder erfolgreichen Änderung `save` auf."""
    while True:
        print("\n=== Aufgabe ===")
        print("(1) Aufgabe erstellen")
        print("(2) Aufgabe bearbeiten")
        print("(3) Aufgabe löschen")
        print("(4) Zurück")
        choice = input("Auswahl: ").strip()

        if choice == "1":
            changed = create_task(tasks, subjects)
        elif choice == "2":
            changed = edit_task(tasks, subjects)
        elif choice == "3":
            changed = delete_task(tasks)
        elif choice == "4":
            return
        else:
            print("⚠️ Ungültige Auswahl. Bitte 1 bis 4 eingeben.")
            continue

        if changed and save is not None:
            save()


if __name__ == "__main__":
    from task_overview import SAMPLE_TASKS, show_tasks

    demo_subjects = ["Grundlagen Programmieren", "Mathematik 1", "Statistik 1",
                     "Principales of Management", "Digital Business"]
    demo_tasks = [dict(task) for task in SAMPLE_TASKS]
    task_menu(demo_tasks, demo_subjects)
    show_tasks(demo_tasks)
