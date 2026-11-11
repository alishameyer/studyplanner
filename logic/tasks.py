from logic.validation import clean_text, iso_day, positive_int

# US01: Fach erfassen

def add_subject(data, name):
    name = clean_text(name, "Fachname")

    for existing_name in data["subjects"]:
        if existing_name.casefold() == name.casefold():
            raise ValueError("Dieses Fach ist bereits vorhanden")

    data["subjects"].append(name)
    return name

# US02: Aufgabe erfassen 

def create_task(data, title, subject, deadline, minutes, priority):

    # Titel überprüfen 
    title = clean_text(title, "Titel")

    # Prüfen, ob das Fach existiert 
    if subject not in data["subjects"]:
        raise ValueError("Dieses Fach existiert nicht.") 

    # Frist überprüfen 
    iso_day(deadline) 

    # Aufwand überprüfen 
    minutes = positive_int(minutes, "Aufwand") 

    # Priorität überprüfen 
    priority = positive_int(priority, "Priorität", 3) 

    # Neue ID bestimmen 
    new_id = data["next_task_id"]

    # Aufgabe erstellen 
    new_task = {
        "id": new_id,
        "title": title,
        "subject": subject, 
        "deadline": deadline, 
        "estimated_minutes": minutes, 
        "priority": priority, 
        "completed": False

    }

    # Aufgaben speicher 
    data["tasks"].append(new_task)

    # Nächste ID erhöhen 
    data["next_task_id"] = new_id + 1 

    return new_task 
        

