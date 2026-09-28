# 📓 STUDYPLANNER

Konsolenanwendung für das Modul **Grundlagen Programmierung** im BSc Wirtschaftsinformatik der FHNW.

> **Projektstatus:** Konzept und Umsetzung in Arbeit. Die beschriebenen Funktionen sind Projektziele. Vor der Abgabe wird dieses README an den tatsächlich implementierten Stand angepasst.

## Analysis

### Problem

Studierende haben Lernaufgaben aus mehreren Fächern mit unterschiedlichen Fristen. Sie müssen einschätzen, wie viel Lernzeit bis zu jeder Frist zur Verfügung steht. Ohne gemeinsame Übersicht ist schwer erkennbar, ob die Zeit ausreicht und wann eine Aufgabe sinnvoll bearbeitet werden kann.

### Scenario

Eine studierende Person startet den Studyplanner im Terminal. Sie erfasst Fächer, Aufgaben mit Aufwand und Frist sowie die verfügbaren Lernminuten für einzelne Tage. Der Studyplanner erstellt einen Plan für offene Aufgaben. Reicht die Zeit bis zu einer Frist nicht aus, zeigt er die fehlenden Minuten an. Die Eingaben werden in einer Datei gespeichert und beim nächsten Start wieder geladen.

### User Stories und Acceptance Criteria

#### US01 – Fächer und Aufgaben erfassen

Als studierende Person möchte ich Fächer und Lernaufgaben erfassen, damit ich meine anstehenden Arbeiten überblicken kann.

#### US02 – Lernzeit erfassen

Als studierende Person möchte ich verfügbare Lernzeit für einzelne Tage erfassen, damit mein Plan meine tatsächliche Zeit berücksichtigt.

#### US03 – Lernplan erstellen

Als studierende Person möchte ich offene Aufgaben auf verfügbare Tage verteilen lassen, damit ich weiss, wann ich für welche Aufgabe lerne.

#### US04 – Zeitmangel erkennen

Als studierende Person möchte ich gewarnt werden, wenn die Lernzeit bis zu einer Frist nicht ausreicht, damit ich meinen Plan anpassen kann.

#### US05 – Aufgabe erledigen

Als studierende Person möchte ich Aufgaben als erledigt markieren, damit sie nicht erneut eingeplant werden.

#### US06 – Daten behalten

Als studierende Person möchte ich meine Daten nach einem Neustart wiederfinden, damit ich den Studyplanner wiederholt nutzen kann.

### Use Cases

| ID | Use Case | Ergebnis |
| --- | --- | --- |
| UC01 | Fach erfassen | Ein neues Fach steht für Aufgaben zur Auswahl. |
| UC02 | Aufgabe erfassen | Eine gültige Aufgabe erscheint in der Übersicht. |
| UC03 | Aufgaben anzeigen | Offene Aufgaben werden nach Fälligkeit angezeigt. |
| UC04 | Lernzeit erfassen | Verfügbare Minuten sind einem Datum zugeordnet. |
| UC05 | Lernplan erstellen | Offene Aufgaben erhalten Lernminuten vor ihrer Frist. |
| UC06 | Engpass anzeigen | Fehlende Minuten pro Aufgabe werden sichtbar. |
| UC07 | Aufgabe erledigen | Die Aufgabe wird beim nächsten Plan nicht mehr berücksichtigt. |
| UC08 | Daten speichern und laden | Nach einem Neustart stehen die Eingaben wieder zur Verfügung. |

### Beispiel für die Abnahme

Eine offene Aufgabe benötigt **120 Minuten** bis Mittwoch. Montag sind **60 Minuten**, Dienstag **30 Minuten** und Donnerstag **90 Minuten** frei. Erwartet werden 60 Minuten am Montag, 30 Minuten am Dienstag, keine Minuten am Donnerstag und eine Warnung über **30 fehlende Minuten**.

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
