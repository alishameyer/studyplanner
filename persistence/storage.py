"""US11/US12: geprüfte JSON-Daten mit atomarem Dateiersatz speichern."""

import json
import os
import tempfile
from pathlib import Path

from logic.validation import clean_text, iso_day, positive_int


def empty_data():
    """
    Liefert bei jedem Aufruf einen unabhängigen leeren Datenbestand.
    """
    return {
        "schema_version": 1, "next_task_id": 1,
        "subjects": [], "tasks": [], "availability": [],
    }


def validate_data(data):
    """Prüft auch Beziehungen; gültiges JSON allein reicht nicht aus."""
    if not isinstance(data, dict):
        raise ValueError("Die Datei muss ein JSON-Objekt enthalten.")
    if type(data.get("schema_version")) is not int:
        raise ValueError("schema_version muss eine ganze Zahl sein.")
    if data["schema_version"] != 1:
        raise ValueError("Nicht unterstützte Dateiversion.")
    for key in ("subjects", "tasks", "availability"):
        if not isinstance(data.get(key), list):
            raise ValueError(f"{key} muss eine Liste sein.")
    names = data["subjects"]
    normalized = [clean_text(name, "Fachname") for name in names]
    if normalized != names:
        raise ValueError("Fachnamen enthalten äussere Leerzeichen.")
    if len({name.casefold() for name in names}) != len(names):
        raise ValueError("Doppelte Fachnamen in der Datei.")
    ids = set()
    for task in data["tasks"]:
        validate_task(task, names, ids)
    next_id = positive_int(data.get("next_task_id"), "next_task_id")
    if next_id <= max(ids, default=0):
        raise ValueError("next_task_id muss grösser als vorhandene IDs sein.")
    days = set()
    for entry in data["availability"]:
        if not isinstance(entry, dict):
            raise ValueError("Lernzeiteintrag muss ein Objekt sein.")
        day = entry.get("date")
        iso_day(day)
        positive_int(entry.get("available_minutes"), "Lernminuten")
        if day in days:
            raise ValueError("Doppelte Lernzeitdaten in der Datei.")
        days.add(day)


def validate_task(task, subjects, ids):
    """Prüft eine gespeicherte Aufgabe und registriert ihre ID."""
    if not isinstance(task, dict):
        raise ValueError("Aufgabe muss ein Objekt sein.")
    task_id = positive_int(task.get("id"), "Aufgaben-ID")
    if task_id in ids:
        raise ValueError("Doppelte Aufgaben-ID in der Datei.")
    ids.add(task_id)
    clean_text(task.get("title"), "Titel")
    if task.get("subject") not in subjects:
        raise ValueError("Eine Aufgabe verweist auf ein unbekanntes Fach.")
    iso_day(task.get("deadline"))
    positive_int(task.get("estimated_minutes"), "Aufwand")
    positive_int(task.get("priority"), "Priorität", 3)
    if type(task.get("completed")) is not bool:
        raise ValueError("completed muss true oder false sein.")


def save_data(file_path, data):
    """Prüft vor dem Schreiben und ersetzt die Datei erst nach Erfolg.

    Die temporäre Datei liegt im selben Verzeichnis. Ein Schreibfehler
    vor os.replace erhält die ursprüngliche Datei. Keine Konsole hier.
    """
    validate_data(data)
    path = Path(file_path)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as stream:
            temporary = Path(stream.name)
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
def reject_duplicate_keys(pairs):
    """
    Verhindert, dass doppelte JSON-Schlüssel still überschrieben werden.
    """
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Doppelter JSON-Schlüssel: {key}")
        result[key] = value
    return result


def load_data(file_path):
    """
    Nur eine fehlende Datei erlaubt leere Daten; sonst Fehler melden.
    """
    try:
        with Path(file_path).open(encoding="utf-8") as stream:
            data = json.load(stream, object_pairs_hook=reject_duplicate_keys)
    except FileNotFoundError:
        return empty_data()
    validate_data(data)
    return data
