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
an und erstellt einen Lernplan. Reicht die Zeit bis zur Frist nicht aus,
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

Der Plan verteilt 60 Minuten auf Montag und 30 Minuten auf Dienstag.
Donnerstag wird für diese Aufgabe nicht verwendet, weil er nach der Frist
liegt. Das Programm zeigt **30 fehlende Minuten** an.


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
- Tage ohne erfasste Lernzeit stehen nicht für die Planung zur Verfügung.
- Die Planung arbeitet mit Minuten pro Tag und ohne konkrete Uhrzeiten.

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
- Vergangene Einträge dürfen gespeichert bleiben, werden aber nicht
  für einen neuen Plan verwendet.

### Lernplan

Der Lernplan wird bei jeder Auswahl der Menüoption neu berechnet.

1. Erledigte Aufgaben ausschliessen.
2. Offene Aufgaben nach früherer Frist, höherer Priorität
   und kleinerer Aufgaben-ID sortieren.
3. Verfügbare Tage ab heute chronologisch berücksichtigen.
4. Minuten bis einschliesslich der jeweiligen Aufgabenfrist verteilen.
5. Nicht einplanbare Minuten als Engpass anzeigen.

Eine Aufgabe kann auf mehrere Tage verteilt werden.
Die gesamte Zuteilung eines Tages darf seine verfügbare Zeit
nicht überschreiten.

Der Plan wird nach Datum gruppiert angezeigt. Jeder Eintrag enthält
Aufgabentitel und zugeteilte Minuten. Die gespeicherten Aufgabenaufwände
und Lernzeiten werden durch die Berechnung nicht verändert.

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

## 👥 Team & Responsibilities

| Person | User Stories | Konkrete Aufgaben |
| --- | --- | --- |
| Alisha | US01, US07, US08 | Fächer erfassen; Lernzeiten erfassen und anzeigen |
| Laura | US02, US03, US05 | Aufgaben erfassen, bearbeiten und als erledigt markieren |
| Xhavid | US04, US09, US10 | Aufgabenübersicht; Lernplan und Engpasswarnungen |
| Valentin | US06, US11, US12 | Fortschrittsübersicht; Daten speichern und laden |

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

> 🚧 In this section, document how your project fulfills each criterion.  
---
The application interacts with the user via the console. Users can:
- View the pizza menu
- Select pizzas and quantities
- See the running total
- Receive an invoice generated as a file

---


### 2. Data Validation

The application validates all user input to ensure data integrity and a smooth user experience. This is implemented in `main-invoice.py` as follows:

- **Menu selection:** When the user enters a pizza number, the program checks if the input is a digit and within the valid menu range:
	```python
	if not choice.isdigit() or not (1 <= int(choice) <= len(menu)):
			print("⚠️ Invalid choice.")
			continue
	```
	This ensures only valid menu items can be ordered.

- **Menu file validation:** When reading the menu file, the program checks for valid price values and skips invalid lines:
	```python
	try:
			menu.append({"name": name, "size": size, "price": float(price)})
	except ValueError:
			print(f"⚠️ Skipping invalid line: {line.strip()}")
	```

- **Main menu options:** The main menu checks for valid options and handles invalid choices gracefully:
	```python
	else:
			print("⚠️ Invalid choice.")
	```

These checks prevent crashes and guide the user to provide correct input, matching the validation requirements described in the project guidelines.

---

---


### 3. File Processing

The application reads and writes data using files:

- **Input file:** `menu.txt` — Contains the pizza menu, one item per line in the format `PizzaName;Size;Price`.
	- Example:
		```
		Margherita;Medium;12.50
		Salami;Large;15.00
		Funghi;Small;9.00
		```
	- The application reads this file at startup to display available pizzas.

- **Output file:** `invoice_001.txt` (and similar) — Generated when an order is completed. Contains a summary of the order, including items, quantities, prices, discounts, and totals.
	- Example:
		```
		Invoice #001
		----------------------
		1x Margherita (Medium)   12.50


		2x Salami (Large)        30.00
		----------------------
		Total:                  42.50
		Discount:                2.50
		Amount Due:             40.00
		```
		- The output file serves as a record for both the user and the pizzeria, ensuring accuracy and transparency.

## ⚙️ Implementation

### Technology
- Python 3.x
- Environment: GitHub Codespaces
- No external libraries

### 📂 Repository Structure
```text
PizzaRP/
├── main.py             # main program logic (console application)
├── menu.txt            # pizza menu (input data file)
├── invoice_001.txt     # example of a generated invoice (output file)
├── docs/               # optional screenshots or project documentation
└── README.md           # project description and milestones
```

### How to Run
> 🚧 Adjust if needed.
1. Open the repository in **GitHub Codespaces**
2. Open the **Terminal**
3. Run:
	```bash
	python3 main.py
	```

### Libraries Used

- `os`: Used for file and path operations, such as checking if the menu file exists and creating new files.
- `glob`: Used to find all invoice files matching a pattern (e.g., `invoice_*.txt`) to determine the next invoice number.

These libraries are part of the Python standard library, so no external installation is required. They were chosen for their simplicity and effectiveness in handling file management tasks in a console application.


## 👥 Team & Contributions

> 🚧 Fill in the names of all team members and describe their individual contributions below. Each student should be responsible for at least one part of the project.

| Name       | Contribution                                 |
|------------|----------------------------------------------|
| Student A  | Menu reading (file input) and displaying menu|
| Student B  | Order logic and data validation              |
| Student C  | Invoice generation (file output) and slides  |


## 🤝 Contributing

> 🚧 This is a template repository for student projects.  
> 🚧 Do not change this section in your final submission.

- Use this repository as a starting point by importing it into your own GitHub account.  
- Work only within your own copy — do not push to the original template.  
- Commit regularly to track your progress.

## 📝 License

This project is provided for **educational use only** as part of the Programming Foundations module.  
[MIT License](LICENSE)
