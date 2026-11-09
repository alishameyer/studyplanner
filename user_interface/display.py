# Lesbare deutsche Konsolenausgaben, keine Änderungen an Projektdaten

from datetime import date
from logic.availability import list_availability

WEEKDAYS = (
    "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag",
)
PRIORITIES = {1: "niedrig", 2: "mittel", 3: "hoch"}


def format_date(value):
    # ISO-Datum in Datum mit deutschem Wochentag umwandeln.
    day = date.fromisoformat(value)
    return f"{day:%d.%m.%Y} ({WEEKDAYS[day.weekday()]})"


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
