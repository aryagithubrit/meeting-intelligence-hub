import re

def assign_priority(task):
    task_lower = task.lower()

    # HIGH PRIORITY
    if "urgent" in task_lower or "asap" in task_lower:
        return "HIGH"

    if "tomorrow" in task_lower or "today" in task_lower:
        return "HIGH"

    # MEDIUM PRIORITY
    if "friday" in task_lower or "next week" in task_lower or "soon" in task_lower:
        return "MEDIUM"

    # DEFAULT
    return "LOW"


def extract_person(line):
    if ":" in line:
        return line.split(":")[0].strip()
    return "Unknown"


def extract_deadline(line):
    line_lower = line.lower()

    # 🔥 detect common deadlines
    if "tomorrow" in line_lower:
        return "Tomorrow"
    if "today" in line_lower:
        return "Today"
    if "friday" in line_lower:
        return "Friday"
    if "monday" in line_lower:
        return "Monday"
    if "next week" in line_lower:
        return "Next Week"

    # 🔥 detect specific dates like April 15
    date_match = re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\s+\d+', line_lower)
    if date_match:
        return date_match.group()

    return "Not specified"


def clean_task(line):
    if ":" in line:
        return line.split(":", 1)[1].strip()
    return line.strip()