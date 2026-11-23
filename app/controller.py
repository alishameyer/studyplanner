"""
Startpunkt: Laden, Menü, Änderungen und Fehleranzeige.
"""

import argparse
from copy import deepcopy
from pathlib import Path

from user_interface.cli import (
    MENU, MUTATING_CHOICES, handle_changes, handle_view,
)

from examples.sample_data import demo_data
from persistence.storage import load_data, save_data


def apply_change(choice, data, file_path):
    """
    Speichert zuerst eine Kopie, Fehler behalten den bisherigen Stand.
    Dadurch zeigt die Anwendung nach einem Schreibfehler keine Änderung als erfolgreich an.
    Weder Originaldaten noch Datei werden absichtlich durch einen ungültigen Bearbeitungsversuch ersetzt.
    """

    candidate = deepcopy(data)
    handle_change(choice, candidate)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    save_data(file_path, candidate)
    return candidate


def run(file_path):
    """
    Ladefehler brechen ab, Bedienfehler führen zurück ins Hauptmenü.
    """
    try:
        data = load_data(file_path)
    except (ValueError, OSError, UnicodeError) as error:
        print(f"Start abgebrochen: {error}")
        print("Die Datendatei wurde nicht überschrieben.")
        return 1
    print(f"Studyplanner – Referenz | Daten: {file_path}")
    while True:
        try:
            print(MENU)
            choice = input("Auswahl: ").strip()
            if choice == "0":
                print("Beendet. Erfolgreiche Änderungen sind gespeichert.")
                return 0
            if choice in MUTATING_CHOICES:
                data = apply_change(choice, data, file_path)
                print("Änderung erfolgreich gespeichert.")
            elif not handle_view(choice, data):
                print("Ungültige Menüauswahl.")
        except (ValueError, OSError, UnicodeError) as error:
            print(f"Aktion abgebrochen: {error}")
            print("Der bisherige Datenbestand bleibt erhalten.")
        except (EOFError, KeyboardInterrupt):
            print("\nBeendet. Nicht abgeschlossene Eingabe verworfen.")
            return 0


def main(argv=None):
    """Startoptionen; --demo legt ausschliesslich eine neue Datei an."""
    parser = argparse.ArgumentParser(description="Studyplanner-Referenz")
    root = Path(__file__).resolve().parents[1]
    default = root / "data" / "studyplanner_data.json"
    parser.add_argument("--data", type=Path, default=default)
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args(argv)
    if args.demo:
        if args.data.exists():
            print("Demo abgebrochen: Zieldatei existiert bereits.")
            return 1
        try:
            save_data(args.data, demo_data())
        except (ValueError, OSError) as error:
            print(f"Demo konnte nicht angelegt werden: {error}")
            return 1
    return run(args.data)


if __name__ == "__main__":
    raise SystemExit(main())
