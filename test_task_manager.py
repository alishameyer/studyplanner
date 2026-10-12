import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from task_manager import task_menu

SUBJECTS = ["Mathematik 1", "Digital Business"]


def make_tasks():
    return [
        {"id": 1, "title": "Woche 1", "subject": "Mathematik 1",
         "deadline": "2099-10-14", "estimated_minutes": 90,
         "priority": 3, "completed": False},
        {"id": 2, "title": "Moodlepoints", "subject": "Digital Business",
         "deadline": "2099-10-05", "estimated_minutes": 20,
         "priority": 1, "completed": True},
    ]


def run_menu(tasks, inputs, save=None):
    output = StringIO()
    with patch("builtins.input", side_effect=inputs), redirect_stdout(output):
        task_menu(tasks, SUBJECTS, save)
    return output.getvalue()


class TaskManagerTest(unittest.TestCase):
    def test_create_task_with_retries(self):
        tasks = make_tasks()
        saves = []
        text = run_menu(tasks, ["1", "", "Serie 2", "9", "2",
                                "2099-12-01", "01-01-2020", "01-12-2099", "0", "60",
                                "5", "2", "4"], lambda: saves.append(1))
        new = tasks[-1]
        self.assertEqual(new, {"id": 3, "title": "Serie 2",
                               "subject": "Digital Business",
                               "deadline": "2099-12-01",
                               "estimated_minutes": 60, "priority": 2,
                               "completed": False})
        self.assertEqual(saves, [1])
        for message in ["Ungültiges Datum", "Titel darf nicht leer", "1 bis 2", "Vergangenheit",
                        "positive ganze", "1, 2 oder 3"]:
            self.assertIn(message, text)

    def test_edit_keeps_id_status_and_empty_inputs(self):
        tasks = make_tasks()
        run_menu(tasks, ["2", "2", "Moodlepoints holen", "", "", "45", "", "4"])
        self.assertEqual(tasks[1], {"id": 2, "title": "Moodlepoints holen",
                                    "subject": "Digital Business",
                                    "deadline": "2099-10-05",
                                    "estimated_minutes": 45, "priority": 1,
                                    "completed": True})

    def test_unknown_id_changes_nothing(self):
        tasks = make_tasks()
        saves = []
        text = run_menu(tasks, ["2", "99", "3", "abc", "4"],
                        lambda: saves.append(1))
        self.assertEqual(tasks, make_tasks())
        self.assertEqual(saves, [])
        self.assertEqual(text.count("Keine Aufgabe mit dieser ID"), 2)

    def test_delete_with_confirmation(self):
        tasks = make_tasks()
        run_menu(tasks, ["3", "1", "n", "3", "1", "j", "4"])
        self.assertEqual([task["id"] for task in tasks], [2])

    def test_create_without_subjects(self):
        tasks = []
        output = StringIO()
        with patch("builtins.input", side_effect=["1", "4"]), redirect_stdout(output):
            task_menu(tasks, [])
        self.assertEqual(tasks, [])
        self.assertIn("zuerst ein Fach", output.getvalue())

    def test_invalid_menu_choice(self):
        self.assertIn("Ungültige Auswahl", run_menu(make_tasks(), ["7", "4"]))


if __name__ == "__main__":
    unittest.main()
