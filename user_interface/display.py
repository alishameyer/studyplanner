from logic.availability import list_availability


def show_availability(data):
    entries = list_availability(data)

    if not entries:
        print("Es sind noch keine Lernzeiten erfasst.")
        return

    total = 0
    for entry in entries:
        day = format_date(entry["date"])
        minutes = entry["available_minutes"]
        print(f"{day}: {minutes} Min.")
        total += minutes

    print(f"Gesamt: {total} Min.")
