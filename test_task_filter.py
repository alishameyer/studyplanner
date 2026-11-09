import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from task_filter import filter_by_subject, show_tasks_by_subject

SUBJECTS = ["Mathematik", "BWL", "Statistik"]


def task(task_id, deadline, subject, completed=False):
    return {"id": task_id, "title": f"Aufgabe {task_id}", "subject": subject,
            "deadline": deadline, "estimated_minutes": 30,
            "priority": 2, "completed": completed}


TASKS = [
    task(1, "2026-10-14", "Mathematik"),
    task(2, "2026-10-09", "BWL"),
    task(3, "2026-10-07", "BWL"),
    task(4, "2026-10-05", "BWL", completed=True),
]


def capture(choice, tasks=TASKS, subjects=SUBJECTS):
    output = StringIO()
    with patch("builtins.input", return_value=choice), redirect_stdout(output):
        show_tasks_by_subject(tasks, subjects)
    return output.getvalue()


class FilterTest(unittest.TestCase):
    def test_only_selected_subject(self):
        self.assertEqual([t["id"] for t in filter_by_subject(TASKS, "BWL")], [2, 3, 4])
        self.assertEqual(filter_by_subject(TASKS, "Statistik"), [])

    def test_subjects_are_numbered(self):
        text = capture("2")
        for expected in ["(1) Mathematik", "(2) BWL", "(3) Statistik"]:
            self.assertIn(expected, text)

    def test_shows_only_chosen_subject_sorted(self):
        text = capture("2")
        self.assertNotIn("Aufgabe 1", text)
        self.assertLess(text.index("Aufgabe 3"), text.index("Aufgabe 2"))
        self.assertGreater(text.index("Aufgabe 4"), text.index("Erledigte"))

    def test_message_for_subject_without_tasks(self):
        self.assertIn("keine Aufgaben", capture("3"))

    def test_invalid_choice(self):
        for choice in ["0", "4", "abc", ""]:
            self.assertIn("Bitte eine Zahl von 1 bis 3", capture(choice))

    def test_message_without_subjects(self):
        self.assertIn("keine Fächer erfasst", capture("1", subjects=[]))


if __name__ == "__main__":
    unittest.main()
