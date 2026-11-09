# Gemeinsame Prüfungen für Konsole, Geschäftslogik und JSON-Dateien.

from datetime import date


def clean_text(value, label):
    # Gibt einen bereinigten, nicht leeren einzeiligen Text zurück.
    if not isinstance(value, str):
        raise ValueError(f"{label} muss Text sein.")
    result = value.strip()
    if not result or any(ord(char) < 32 for char in result):
        raise ValueError(f"{label} darf nicht leer oder mehrzeilig sein.")
    return result


def positive_int(value, label, maximum=None):
    # Prüft echte ganze Zahlen; bool zählt hier nicht als Zahl.
    if type(value) is not int or value < 1:
        raise ValueError(f"{label} muss eine positive ganze Zahl sein.")
    if maximum is not None and value > maximum:
        raise ValueError(f"{label} darf höchstens {maximum} sein.")
    return value


def iso_day(value):
    """Prüft ein gültiges Datum in genau YYYY-MM-DD."""
    if not isinstance(value, str):
        raise ValueError("Datum muss Text im Format YYYY-MM-DD sein.")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError("Ungültiges Datum: YYYY-MM-DD verwenden.") from error
    if parsed.isoformat() != value:
        raise ValueError("Datum muss das Format YYYY-MM-DD haben.")
    return parsed
