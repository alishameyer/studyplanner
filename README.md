# 📓 STUDYPLANNER

Konsolenanwendung für das Modul **Grundlagen Programmierung**
im BSc Wirtschaftsinformatik der FHNW.

> **Projektstatus:** In Entwicklung. Die beschriebenen Funktionen
> sind Projektziele.


## 📝 Analysis

### Problem

Studierende haben Lernaufgaben aus mehreren Fächern mit unterschiedlichen
Fristen. Ohne gemeinsame Übersicht ist schwer erkennbar, welche Aufgaben
anstehen und ob die verfügbare Lernzeit bis zur jeweiligen Frist ausreicht.

### Scenario

Eine studierende Person erfasst Fächer, Lernaufgaben und verfügbare
Lernminuten in der Konsole. Der Studyplanner zeigt Aufgaben und Fortschritt
an. Reicht die Zeit bis zur Frist nicht aus,
zeigt er die fehlenden Minuten an. Die Daten bleiben nach einem Neustart
erhalten.

### User Stories und Acceptance Criteria

<img width="592" height="642" alt="user-stories drawio" src="https://github.com/user-attachments/assets/09237b59-6b9f-47f0-80a0-d824693cc0c5" />

#### Fächer und Aufgaben

**US01 – Fach erfassen: Alisha**

Als studierende Person möchte ich Fächer erfassen,
damit ich Aufgaben einem Fach zuordnen kann.

- Fachnamen dürfen nicht leer sein.
- Bereits vorhandene Fachnamen werden nicht doppelt angelegt.
- Ein erfasstes Fach steht bei der Aufgabenerfassung zur Auswahl.

**US02 – Aufgabe erfassen: Laura**

Als studierende Person möchte ich Lernaufgaben erfassen,
damit ich weiss, was ich bis wann erledigen muss.

- Eine Aufgabe enthält Titel, vorhandenes Fach, gültige Frist,
  positive ganze Minutenzahl und Priorität von 1 bis 3.
- Jede Aufgabe erhält eine eindeutige ID und den Status „offen“.
- Ungültige Eingaben werden verständlich gemeldet und nicht gespeichert.

**US03 – Aufgabe bearbeiten: Laura**

Als studierende Person möchte ich Aufgaben bearbeiten,
damit ich Änderungen an Inhalt, Frist oder Aufwand berücksichtigen kann.

- Eine Aufgabe kann über ihre ID ausgewählt und bearbeitet werden.
- Geänderte Angaben werden wie bei der Erfassung geprüft.
- Die ID und der Status bleiben erhalten; unbekannte IDs verändern nichts.

#### Übersicht und Fortschritt

**US04 – Aufgaben anzeigen: Xhavid**

Als studierende Person möchte ich meine Aufgaben nach Frist anzeigen,
damit ich erkenne, welche Aufgaben als Nächstes anstehen.

- Offene Aufgaben werden nach aufsteigender Frist angezeigt.
- Die Übersicht enthält ID, Titel, Fach, Frist, Aufwand und Priorität;
  erledigte Aufgaben werden getrennt angezeigt.
- Ohne Aufgaben erscheint eine verständliche Meldung.

**US05 – Aufgabe erledigen: Laura**

Als studierende Person möchte ich Aufgaben als erledigt markieren,
damit abgeschlossene Aufgaben nicht erneut eingeplant werden.

- Eine vorhandene offene Aufgabe kann über ihre ID erledigt werden.
- Die Änderung wird bestätigt und ist in der Übersicht sichtbar.
- Bei der nächsten Planberechnung wird die Aufgabe ausgeschlossen.

**US06 – Fortschritt anzeigen: Valentin**

Als studierende Person möchte ich meinen Fortschritt sehen,
damit ich erkenne, wie viele Aufgaben abgeschlossen sind.

- Die Anzahl aller, offenen und erledigten Aufgaben wird angezeigt.
- Der Prozentanteil erledigter Aufgaben wird korrekt berechnet.
- Ohne Aufgaben werden 0 Aufgaben und 0 % angezeigt.

#### Lernzeiten und Planung

**US07 – Lernzeit erfassen: Alisha**

Als studierende Person möchte ich verfügbare Lernminuten pro Tag erfassen,
damit der Plan meine tatsächliche Zeit berücksichtigt.

- Ein gültiges Datum und eine positive ganze Minutenzahl werden akzeptiert.
- Eine neue Eingabe für denselben Tag ersetzt den bisherigen Wert.
- Ungültige Angaben werden verständlich gemeldet und nicht übernommen.

**US08 – Lernzeiten anzeigen: Alisha**

Als studierende Person möchte ich meine Lernzeiten anzeigen,
damit ich die erfasste Verfügbarkeit überprüfen kann.

- Die Einträge werden chronologisch mit Datum und Minuten angezeigt.
- Die Summe der angezeigten Minuten wird ausgegeben.
- Ohne Einträge erscheint eine verständliche Meldung.

**US09 – Aufgaben nach Fach filtern: Xhavid**

Als studierende Person möchte ich Aufgaben eines bestimmten Fachs anzeigen, damit ich mich gezielt auf ein Fach konzentrieren kann. 

- Vorhandene Fächer werden nummeriert zur Auswahl angezeigt. 
- Es werden nur die Aufgaben des gewählten Fachs nach aufsteigender Frist angezeigt; offene     und erledigte getrennt. 
- Hat das Fach keine Aufgaben, erscheint eine verständliche Meldung. 

#### Engpässe und Speicherung

**US10 – Zeitmangel erkennenz: Xhavid**

Als studierende Person möchte ich Engpässe erkennen,
damit ich bei fehlender Lernzeit rechtzeitig reagieren kann.

- Für nicht vollständig eingeplante Aufgaben werden Titel, Frist
  und fehlende Minuten angezeigt.
- Fehlende Minuten entsprechen dem Aufwand abzüglich eingeplanter Minuten.
- Überfällige offene Aufgaben werden gekennzeichnet;
  vollständig eingeplante Aufgaben erhalten keine Engpasswarnung.

**US11 – Daten speichern: Valentin**

Als studierende Person möchte ich meine Eingaben speichern,
damit meine Arbeit beim Beenden erhalten bleibt.

- Erfolgreiche Änderungen an Fächern, Aufgaben und Lernzeiten
  werden automatisch in einer JSON-Datei gespeichert.
- Aufgabenstatus und Umlaute bleiben erhalten.
- Schreibfehler werden gemeldet; das Programm meldet keinen falschen Erfolg.

**US12 – Daten laden: Valentin**

Als studierende Person möchte ich gespeicherte Daten beim Start laden,
damit ich mit meinen bisherigen Eingaben weiterarbeiten kann.

- Gespeicherte Daten werden inklusive Aufgaben-IDs und Status geladen;
  neue Aufgaben erhalten weiterhin eindeutige IDs.
- Fehlt die Datei beim ersten Start, beginnt das Programm mit leeren Daten.
- Beschädigte oder ungültig aufgebaute Dateien werden verständlich
  gemeldet und nicht automatisch überschrieben.

### Use Cases

| ID | Use Case | User Story |
| --- | --- | --- |
| UC01 | Fach erfassen | US01 |
| UC02 | Aufgabe erfassen | US02 |
| UC03 | Aufgabe bearbeiten | US03 |
| UC04 | Aufgaben anzeigen | US04 |
| UC05 | Aufgabe erledigen | US05 |
| UC06 | Fortschritt anzeigen | US06 |
| UC07 | Lernzeit erfassen | US07 |
| UC08 | Lernzeiten anzeigen | US08 |
| UC09 | Aufgaben nach Fach filtern | US09 |
| UC10 | Zeitmangel erkennen | US10 |
| UC11 | Daten speichern | US11 |
| UC12 | Daten laden | US12 |

### Beispiel für die Abnahme

Eine Aufgabe benötigt **120 Minuten** bis Mittwoch.
Montag sind **60 Minuten**, Dienstag **30 Minuten**
und Donnerstag **90 Minuten** verfügbar.

## 👥 Team & Responsibilities

| Person | User Stories | Konkrete Aufgaben |
| --- | --- | --- |
| Alisha | US01, US07, US08 | Fächer erfassen; Lernzeiten erfassen und anzeigen |
| Laura | US02, US03, US05 | Aufgaben erfassen, bearbeiten und als erledigt markieren |
| Xhavid | US04, US09, US10 | Aufgabenübersicht; Lernplan und Engpasswarnungen |
| Valentin | US06, US11, US12 | Fortschrittsübersicht; Daten speichern und laden |

## ⚙️ Geplante Umsetzung

### Bedienung

Der Studyplanner wird über ein nummeriertes Konsolenmenü bedient.
Nach einer Aktion erscheint das Hauptmenü erneut.

| Auswahl | Aktion |
| --- | --- |
| 1 | Fach erfassen |
| 2 | Aufgabe erfassen |
| 3 | Aufgabe bearbeiten |
| 4 | Aufgaben anzeigen |
| 5 | Aufgabe erledigen |
| 6 | Fortschritt anzeigen |
| 7 | Lernzeit erfassen |
| 8 | Lernzeiten anzeigen |
| 9 | Aufgaben nach Fach filtern |
| 10 | Engpässe anzeigen |
| 0 | Programm beenden |

Speichern und Laden erfolgen automatisch. Sie benötigen keine
eigenen Menüoptionen.

### Darstellung der Tage

Wir verwenden konkrete Datumsangaben statt wiederkehrender Wochentage.

- Eingabe: `YYYY-MM-DD`, beispielsweise `2026-10-05`.
- Anzeige: Datum und Wochentag, beispielsweise `05.10.2026 (Montag)`.
- Der Wochentag wird aus dem Datum berechnet.
- Pro Datum wird eine verfügbare Minutenzahl gespeichert.

Beispiel für die Anzeige der Lernzeiten:

| Datum | Verfügbare Lernzeit |
| --- | --- |
| 05.10.2026 (Montag) | 60 Minuten |
| 06.10.2026 (Dienstag) | 30 Minuten |
| 08.10.2026 (Donnerstag) | 90 Minuten |

Die Konsolenausgabe zeigt dieselben Angaben als einfache Textliste.

### Fächer und Aufgaben

Fächer werden über ihren Namen erfasst. Bei der Aufgabenerfassung
werden vorhandene Fächer nummeriert angezeigt und ausgewählt.

Eine Aufgabe enthält:

| Feld | Bedeutung |
| --- | --- |
| `id` | Eindeutige Aufgaben-ID |
| `title` | Aufgabentitel |
| `subject` | Zugeordnetes Fach |
| `deadline` | Fälligkeitsdatum |
| `estimated_minutes` | Geschätzter Aufwand in Minuten |
| `priority` | 1 = niedrig, 2 = mittel, 3 = hoch |
| `completed` | Offen oder erledigt |

Neue Aufgaben sind offen. Beim Bearbeiten bleiben ID und Status erhalten.
Bei der Auswahl einer unbekannten ID erscheint eine Fehlermeldung.

### Lernzeiten

Lernzeiten werden mit Datum und verfügbaren Minuten erfasst.

- Neue Lernzeiten dürfen für heute oder einen zukünftigen Tag erfasst werden.
- Pro Datum gibt es genau einen Eintrag.
- Bei erneuter Eingabe für dasselbe Datum wird der bisherige Wert ersetzt.
- Die Übersicht zeigt die Einträge chronologisch und ihre Gesamtsumme.

### Speicherung

Fächer, Aufgaben und Lernzeiten werden als Listen und Dictionaries
in `studyplanner_data.json` gespeichert.

- Beim Start werden vorhandene Daten geladen.
- Nach erfolgreichen Änderungen werden die Daten gespeichert.
- Der berechnete Plan wird nicht gespeichert, sondern neu erzeugt.
- Fehlt die Datei beim ersten Start, beginnt das Programm mit leeren Daten.
- Bei beschädigten Daten wird der normale Start abgebrochen und
  eine verständliche Meldung angezeigt. Die Datei bleibt erhalten.
- Schreibfehler werden gemeldet und nicht als erfolgreiche Speicherung
  dargestellt.

### Parallele Entwicklung

Vor der Umsetzung vereinbaren wir die gemeinsamen Datenfelder:

- Fächer: Liste mit Fachnamen.
- Aufgaben: Liste mit Dictionaries und den Feldern `id`, `title`,
  `subject`, `deadline`, `estimated_minutes`, `priority` und `completed`.
- Lernzeiten: Liste mit Dictionaries und den Feldern `date`
  und `available_minutes`.
- JSON-Datei: Dictionary mit den Bereichen `subjects`, `tasks`
  und `availability`.

Alle verwenden dieselben Beispieldaten. So müssen die Funktionen
anderer Personen noch nicht fertig sein, um die eigene Arbeit zu prüfen.

| Person | Einstieg ohne Wartezeit |
| --- | --- |
| Alisha | Fächer und Lernzeiten mit zunächst leeren Listen erfassen |
| Laura | Aufgaben mit einer vorbereiteten Fächerliste erfassen und bearbeiten |
| Xhavid | Beispielaufgaben anzeigen und mit vorbereiteten Lernzeiten planen |
| Valentin | Fortschritt aus Beispielaufgaben berechnen und Beispieldaten speichern und laden |

### Gemeinsame Integration

- Jede Person implementiert und prüft ihre drei User Stories.
- Änderungen erfolgen hauptsächlich in den eigenen Modulen.
- `main.py` wird schrittweise ergänzt. Pro Änderung arbeitet nur eine
  abgesprochene Person daran.
- Valentin stellt Funktionen zum Speichern und Laden bereit.
  Die anderen Module führen keine eigenen Dateioperationen aus.
- Nach einer erfolgreichen Änderung ruft `main.py` die Speicherfunktion auf.
- Jede Person erstellt eigene Commits und Pull Requests.
- Nach dem Zusammenführen prüfen wir den gemeinsamen Programmablauf.

---

## ✅ Project Requirements

Each app must meet the following three criteria in order to be accepted (see also the official project guidelines PDF on Moodle):

1. Interactive app (console input)
2. Data validation (input checking)
3. File processing (read/write)

---

### 1. Interactive App (Console Input)

Der Studyplanner wird über ein nummeriertes Hauptmenü in der Konsole bedient
(siehe Tabelle "Bedienung"). Nach jeder Aktion erscheint das Menü erneut.
Bereits in `main.py` eingebunden:

- **(4) Aufgaben anzeigen:** offene Aufgaben nach Frist, erledigte getrennt (US04)
- **(9) Aufgaben nach Fach filtern:** Fach aus nummerierter Liste wählen (US09)
- **(10) Engpässe anzeigen:** fehlende Minuten und überfällige Aufgaben (US10)
- **(0) Programm beenden**

Die übrigen Optionen werden ergänzt, sobald die zugehörigen User Stories
umgesetzt sind.

---

### 2. Data Validation

Eingaben werden geprüft, bevor sie übernommen werden. Ungültige Eingaben
werden verständlich gemeldet und nicht gespeichert.

- **Menüauswahl:** Unbekannte Optionen werden abgewiesen:
	```python
	else:
	    print("⚠️ Ungültige Auswahl.")
	```

- **Fachauswahl** (`task_overview.py`): Nur Zahlen im gültigen Bereich
  werden akzeptiert:
	```python
	if not choice.isdigit() or not 1 <= int(choice) <= len(subjects):
	    print(f"⚠️ Bitte eine Zahl von 1 bis {len(subjects)} wählen.")
	```

- **Aufgabenfelder** (`task_manager.py`): Titel nicht leer, Frist im Format
  `DD-MM-YYYY` und nicht in der Vergangenheit, Aufwand als positive ganze
  Minutenzahl, Priorität 1 bis 3:
	```python
	if not text.isdigit() or int(text) <= 0:
	    raise ValueError("Der Aufwand muss eine positive ganze Minutenzahl sein.")
	```

---

### 3. File Processing

Fächer, Aufgaben und Lernzeiten werden in `studyplanner_data.json`
gespeichert und beim Start wieder geladen (US11, US12).

- **Datei:** `studyplanner_data.json` — Dictionary mit den Bereichen
  `subjects`, `tasks` und `availability`.
	- Beispiel:
		```json
		{
		  "subjects": ["Mathematik 1", "Digital Business"],
		  "tasks": [
		    {"id": 1, "title": "Woche 1", "subject": "Mathematik 1",
		     "deadline": "2026-10-14", "estimated_minutes": 90,
		     "priority": 3, "completed": false}
		  ],
		  "availability": [
		    {"date": "2026-11-06", "available_minutes": 60}
		  ]
		}
		```
- Die Datei im Repository enthält die gemeinsamen Beispieldaten.
- Fehlt die Datei, startet das Programm mit leeren Daten; beschädigte
  Dateien werden gemeldet und nicht überschrieben.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
studyplanner/
├── main.py                  # Hauptmenü (Konsolenanwendung)
├── task_overview.py         # US04 Aufgaben anzeigen, US09 nach Fach filtern
├── task_shortage.py         # US10 Zeitmangel erkennen
├── task_manager.py          # US02 Aufgabe erfassen, US03 bearbeiten
├── studyplanner_data.json   # Fächer, Aufgaben und Lernzeiten (Beispieldaten)
├── test_*.py                # Unit-Tests (unittest)
└── README.md                # Projektbeschreibung
```

### How to Run
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```
4. Run the tests:
	```bash
	python3 -m unittest
	```

### Libraries Used

- `datetime`: Prüft Datumsangaben, vergleicht Fristen und berechnet den
  Wochentag für die Anzeige (`05.10.2026 (Montag)`).
- `json`: Speichert und lädt die Daten in `studyplanner_data.json`.
- `unittest`: Automatische Tests der einzelnen Module.

These libraries are part of the Python standard library, so no external installation is required.


## 👥 Team & Contributions

| Name     | Contribution |
|----------|--------------|
| Alisha   | US01, US07, US08: Fächer erfassen; Lernzeiten erfassen und anzeigen |
| Laura    | US02, US03, US05: Aufgaben erfassen, bearbeiten und als erledigt markieren |
| Xhavid   | US04, US09, US10: Aufgabenübersicht, Filter nach Fach, Engpasswarnungen |
| Valentin | US06, US11, US12: Fortschrittsübersicht; Daten speichern und laden |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
