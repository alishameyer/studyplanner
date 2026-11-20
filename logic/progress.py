"""US06: Anzahl offener und erledigter Aufgaben und Prozentanteil."""


def calculate_progress(data):
    """
    Berechnet ausschliesslich die aufgabenbezogenen Kennzahlen.
    """
    tasks = data["tasks"]
    total = len(tasks)
    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1
    return {
        "total": total, "completed": completed, "open": total - completed,
        "percentage": 100 * completed / total if total else 0,
    }