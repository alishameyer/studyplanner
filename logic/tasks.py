from logic.validation import clean_text, iso_day, positive_int


def add_subject(data, name):
    name = clean_text(name, "Fachname")

    for existing_name in data["subjects"]:
        if existing_name.casefold() == name.casefold():
            raise ValueError("Dieses Fach ist bereits vorhanden")

    data["subjects"].append(name)
    return name
