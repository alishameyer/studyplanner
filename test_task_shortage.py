import unittest
from datetime import date

from task_overview import filter_by_subject
from task_shortage import find_shortages, planned_minutes

AVAILABILITY = [
    {"date": "2026-10-05", "available_minutes": 60},
    {"date": "2026-10-06", "available_minutes": 30},
    {"date": "2026-10-08", "available_minutes": 90},
]


def task(task_id, deadline, minutes, subject="Mathematik", completed=False):
    return {"id": task_id, "title": f"Aufgabe {task_id}", "subject": subject,
            "deadline": deadline, "estimated_minutes": minutes,
            "priority": 2, "completed": completed}


class ShortageTest(unittest.TestCase):
    def test_readme_example_is_short_by_30(self):
        # 120 Min. bis Mittwoch (07.10.): nur Montag + Dienstag = 90 Min.
        tasks = [task(1, "2026-10-07", 120)]
        self.assertEqual(planned_minutes(tasks, AVAILABILITY), {1: 90})
        shortages = find_shortages(tasks, AVAILABILITY, date(2026, 10, 1))
        self.assertEqual([(t["id"], m, o) for t, m, o in shortages], [(1, 30, False)])

    def test_fully_planned_task_has_no_warning(self):
        tasks = [task(1, "2026-10-08", 120)]
        self.assertEqual(find_shortages(tasks, AVAILABILITY, date(2026, 10, 1)), [])

    def test_overdue_open_task_is_flagged(self):
        tasks = [task(1, "2026-09-01", 30)]
        shortages = find_shortages(tasks, AVAILABILITY, date(2026, 10, 1))
        self.assertTrue(shortages[0][2])

    def test_completed_tasks_are_ignored(self):
        tasks = [task(1, "2026-09-01", 30, completed=True)]
        self.assertEqual(find_shortages(tasks, AVAILABILITY, date(2026, 10, 1)), [])


class FilterTest(unittest.TestCase):
    def test_only_selected_subject(self):
        tasks = [task(1, "2026-10-07", 10, "Mathematik"), task(2, "2026-10-07", 10, "BWL")]
        self.assertEqual([t["id"] for t in filter_by_subject(tasks, "BWL")], [2])
        self.assertEqual(filter_by_subject(tasks, "Statistik"), [])


if __name__ == "__main__":
    unittest.main()
