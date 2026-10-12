import unittest
from contextlib import redirect_stdout
from io import StringIO

from task_overview import format_date, show_tasks, split_tasks

SAMPLE_TASKS = [
    {"id": 1, "title": "Übungsblatt 3", "subject": "Mathematik",
     "deadline": "2026-10-14", "estimated_minutes": 90,
     "priority": 2, "completed": False},
    {"id": 2, "title": "Zusammenfassung Kapitel 2", "subject": "BWL",
     "deadline": "2026-10-07", "estimated_minutes": 120,
     "priority": 3, "completed": False},
    {"id": 3, "title": "Quiz vorbereiten", "subject": "Programmieren",
     "deadline": "2026-10-05", "estimated_minutes": 45,
     "priority": 1, "completed": True},
]


def capture(tasks):
    output = StringIO()
    with redirect_stdout(output):
        show_tasks(tasks)
    return output.getvalue()


class TaskOverviewTest(unittest.TestCase):
    def test_open_tasks_sorted_by_deadline(self):
        open_tasks, _ = split_tasks(SAMPLE_TASKS)
        self.assertEqual([task["id"] for task in open_tasks], [2, 1])

    def test_completed_tasks_separated(self):
        open_tasks, done_tasks = split_tasks(SAMPLE_TASKS)
        self.assertTrue(all(not task["completed"] for task in open_tasks))
        self.assertEqual([task["id"] for task in done_tasks], [3])

    def test_overview_contains_all_fields(self):
        text = capture(SAMPLE_TASKS)
        for expected in ["ID 2: ", "Zusammenfassung Kapitel 2", "BWL",
                         "07.10.2026 (Mittwoch)", "120 Min.", "hoch"]:
            self.assertIn(expected, text)
        self.assertLess(text.index("Offene"), text.index("Erledigte"))
        self.assertGreater(text.index("Quiz vorbereiten"), text.index("Erledigte"))

    def test_message_without_tasks(self):
        self.assertIn("keine Aufgaben erfasst", capture([]))

    def test_format_date(self):
        self.assertEqual(format_date("2026-10-05"), "05.10.2026 (Montag)")


if __name__ == "__main__":
    unittest.main()
