"""Aufgaben verwalten: erstellen (US02), bearbeiten (US03) und löschen.

Das Untermenü "Aufgabe" bietet:
(1) Aufgabe erstellen, (2) Aufgabe bearbeiten, (3) Aufgabe löschen,
(4) Zurück

Das Modul liest und schreibt keine Dateien. Nach einer erfolgreichen
Änderung wird die übergebene Funktion `save` aufgerufen.
"""

from datetime import date

from task_overview import PRIORITIES, format_task

DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# ---------- Datum prüfen ----------

def is_leap_year(year):
    """Gibt True zurück, wenn das Jahr ein Schaltjahr ist."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def is_valid_date(text):
    """Prüft, ob der Text ein echtes Datum im Format DD-MM-YYYY ist."""
    parts = text.split("-")
    if len(parts) != 3:
        return False
    day, month, year = parts
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return False
    if len(year) != 4 or int(month) < 1 or int(month) > 12:
        return False

    last_day = DAYS_PER_MONTH[int(month) - 1]
    if int(month) == 2 and is_leap_year(int(year)):
        last_day = 29
    return 1 <= int(day) <= last_day


def to_iso_date(text):
    """Wandelt '1-12-2099' in '2099-12-01' um."""
    day, month, year = text.split("-")
    if len(day) == 1:
        day = "0" + day
    if len(month) == 1:
        month = "0" + month
    return f"{year}-{month}-{day}"


def to_input_date(iso_date):
    """Wandelt '2099-12-01' in die Eingabeform '01-12-2099' um."""
    return f"{iso_date[8:10]}-{iso_date[5:7]}-{iso_date[0:4]}"


# ---------- Eingaben ----------
# Wird `current` übergeben (beim Bearbeiten), behält eine leere
# Eingabe den bisherigen Wert.

def ask_title(prompt, current=None):
    while True:
        text = input(prompt).strip()
        if text == "" and current is not None:
            return current
        if text != "":
            return text
        print("⚠️ Der Titel darf nicht leer sein.")


def ask_subject(subjects, current=None):
    for number in range(1, len(subjects) + 1):
        print(f"  ({number}) {subjects[number - 1]}")

    while True:
        text = input("Auswahl: ").strip()
        if text == "" and current is not None:
            return current
        if text.isdigit() and 1 <= int(text) <= len(subjects):
            return subjects[int(text) - 1]
        print(f"⚠️ Bitte eine Zahl von 1 bis {len(subjects)} wählen.")


def ask_deadline(prompt, current=None):
    today = str(date.today())  # z. B. "2026-11-09"
    while True:
        text = input(prompt).strip()
        if text == "" and current is not None:
            return current
        if not is_valid_date(text):
            print("⚠️ Ungültiges Datum. Bitte im Format DD-MM-YYYY "
                  "eingeben.")
        elif to_iso_date(text) < today:
            print("⚠️ Die Frist darf nicht in der Vergangenheit liegen.")
        else:
            return to_iso_date(text)


def ask_minutes(prompt, current=None):
    while True:
        text = input(prompt).strip()
        if text == "" and current is not None:
            return current
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("⚠️ Der Aufwand muss eine positive ganze Minutenzahl sein.")


def ask_priority(prompt, current=None):
    while True:
        text = input(prompt).strip()
        if text == "" and current is not None:
            return current
        if text == "1" or text == "2" or text == "3":
            return int(text)
        print("⚠️ Die Priorität muss 1, 2 oder 3 sein.")


# ---------- Aufgaben suchen ----------

def find_task(tasks, text):
    """Sucht eine Aufgabe über ihre ID; gibt None zurück, wenn sie fehlt."""
    text = text.strip()
    if not text.isdigit():
        return None
    for task in tasks:
        if task["id"] == int(text):
            return task
    return None


def choose_task(tasks):
    """Zeigt alle Aufgaben mit ID und fragt nach der gewünschten ID."""
    for task in tasks:
        print("  " + format_task(task))
    return find_task(tasks, input("ID der Aufgabe (Zahl nach 'ID'): "))


def next_id(tasks):
    """Gibt die nächste freie ID zurück (grösste ID + 1)."""
    highest = 0
    for task in tasks:
        if task["id"] > highest:
            highest = task["id"]
    return highest + 1


# ---------- Aktionen ----------

def create_task(tasks, subjects):
    """Erfasst eine neue offene Aufgabe. Gibt True bei Erfolg zurück."""
    print("\n--- Aufgabe erstellen ---")
    if len(subjects) == 0:
        print("⚠️ Bitte zuerst ein Fach erfassen.")
        return False

    title = ask_title("Titel: ")
    print("Fach:")
    subject = ask_subject(subjects)
    deadline = ask_deadline("Frist (DD-MM-YYYY): ")
    minutes = ask_minutes("Aufwand in Minuten: ")
    priority = ask_priority("Priorität (1 = niedrig, 2 = mittel, "
                            "3 = hoch): ")

    task = {"id": next_id(tasks), "title": title, "subject": subject,
            "deadline": deadline, "estimated_minutes": minutes,
            "priority": priority, "completed": False}
    tasks.append(task)
    print(f"✅ Aufgabe erstellt: {format_task(task)}")
    return True


def edit_task(tasks, subjects):
    """Bearbeitet eine Aufgabe; ID und Status bleiben gleich."""
    print("\n--- Aufgabe bearbeiten ---")
    task = choose_task(tasks)
    if task is None:
        print("⚠️ Keine Aufgabe mit dieser ID gefunden.")
        return False

    print(format_task(task))
    print("Leere Eingabe behält den bisherigen Wert.")
    old_deadline = to_input_date(task["deadline"])
    old_priority = f"{task['priority']} = {PRIORITIES[task['priority']]}"

    title = ask_title(f"Titel [{task['title']}]: ", task["title"])
    print(f"Fach [{task['subject']}]:")
    subject = ask_subject(subjects, task["subject"])
    deadline = ask_deadline(f"Frist (DD-MM-YYYY) [{old_deadline}]: ",
                            task["deadline"])
    minutes = ask_minutes(f"Aufwand in Minuten "
                          f"[{task['estimated_minutes']}]: ",
                          task["estimated_minutes"])
    priority = ask_priority(f"Priorität [{old_priority}]: ",
                            task["priority"])

    task["title"] = title
    task["subject"] = subject
    task["deadline"] = deadline
    task["estimated_minutes"] = minutes
    task["priority"] = priority
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
    answer = input("Wirklich löschen? (j/n): ").strip()
    if answer != "j" and answer != "J":
        print("Löschen abgebrochen.")
        return False
    tasks.remove(task)
    print("✅ Aufgabe gelöscht.")
    return True


# ---------- Untermenü ----------

def task_menu(tasks, subjects, save=None):
    """Untermenü "Aufgabe". Ruft nach jeder Änderung `save` auf."""
    while True:
        print("\n=== Aufgabe ===")
        print("(1) Aufgabe erstellen")
        print("(2) Aufgabe bearbeiten")
        print("(3) Aufgabe löschen")
        print("(4) Zurück")
        choice = input("Auswahl: ").strip()

        changed = False
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

        if changed and save is not None:
            save()


if __name__ == "__main__":
    from task_overview import SAMPLE_TASKS, show_tasks

    demo_subjects = ["Grundlagen Programmieren", "Mathematik 1",
                     "Statistik 1", "Principales of Management",
                     "Digital Business"]
    demo_tasks = []
    for sample_task in SAMPLE_TASKS:
        demo_tasks.append(sample_task.copy())
    task_menu(demo_tasks, demo_subjects)
    show_tasks(demo_tasks)
