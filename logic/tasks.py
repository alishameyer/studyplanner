from logic.validation import clean_text, iso_day, positive_int


def add_subject(data, name):
    name = clean_text(name, "Fachname")

    for existing_name in data["subjects"]:
        if existing_name.casefold() == name.casefold():
            raise ValueError("Dieses Fach ist bereits vorhanden")

    data["subjects"].append(name)
    return name

# US05 - Aufgabe erledigen 
def complete_task(data, task_id): 

    task_id = positive_int(task_id, "ID") 

    # Aufgabe anhand der ID suchen 
    for task in data["tasks"]: 

        if task["id"] == task_id: 

            # Prüfen, ob die Aufgabe bereits erledigt ist
            if task["completed"] == True: 
                raise ValueError("DIese Aufgabe ist bereits erledigt.") 

            # Aufgabe als erledigt markieren 
            task["completed"] = True 

            return task 

# Wenn die ID nicht gefunden wurde 
raise ValueError("Diese Aufgaben-ID existiert nicht.")
