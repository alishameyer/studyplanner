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

# US05 - Aufgabe erledigen 
def complete_task(data, task_id):
                     
    task_id = positive_int(task_id, "ID")                
     
    # Aufgabe anhand der ID suchen 
    for task in data["tasks"]: 
         
        if task["id"] == task_id: 
                     
            # Prüfen, ob die Aufgabe bereits erledigt ist
            if task["completed"] == True:
                raise ValueError("Diese Aufgabe ist bereits erledigt.")

            # Aufgabe als erledigt markieren
            task["completed"] = True

            return task

    # Wenn die ID nicht gefunden wurde
    raise ValueError("Diese Aufgaben-ID existiert nicht.")
