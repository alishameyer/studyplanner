from logic.validation import clean_text, iso_day, positive_int


def add_subject(data, name):
    name = clean_text(name, "Fachname")

    for existing_name in data["subjects"]:
        if existing_name.casefold() == name.casefold():
            raise ValueError("Dieses Fach ist bereits vorhanden")

    data["subjects"].append(name)
    return name

# US03 - Aufgabe bearbeiten
def edit_task(data, task_id, title, subject, deadline, minutes, priority):

    task_id = positive_int(task_id, "ID")

    # Aufgabe anhand der ID suchen
    for task in data["tasks"]:

        if task["id"] == task_id:

            # Neue Angaben prüfen
            title = clean_text(title, "Titel")

            if subject not in data["subjects"]:
                raise ValueError("Dieses Fach existiert nicht.")

            iso_day(deadline)
            minutes = positive_int(minutes, "Aufwand")
            priority = positive_int(priority, "Priorität", 3)

            # Aufgabe bearbeiten
            task["title"] = title
            task["subject"] = subject
            task["deadline"] = deadline
            task["estimated_minutes"] = minutes
            task["priority"] = priority

            return task

    # Wenn keine Aufgabe mit dieser ID gefunden wurde
    raise ValueError("Diese Aufgaben-ID existiert nicht.")
