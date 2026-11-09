from logic.validation import iso_day, positive_int


def set_availability(data, day, minutes):
    iso_day(day)
    positive_int(minutes, "Lernminuten")

    for entry in data["availability"]:
        if entry["date"] == day:
            entry["availability_minutes"] = minutes
            return

    data["availability"].append({
        "date": day,
        "availability_minutes": minutes,
    })


def availability_order(entry):
    return entry["date"]


def list_availability(data):
    return sorted(data["availability"], key=availability_order)
