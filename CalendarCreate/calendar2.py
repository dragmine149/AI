import re


class Activities:
    def __init__(self, filename):
        self.activities = []
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        for i in range(len(lines)):
            parts = re.match(r'^(\d{2}/\d{2}/\d{2})(?:\s*-\s*(.*))?', lines[i])
            if parts:
                date = parts.group(1)
                if parts.group(2):
                    activity_parts = re.match(
                        r'L(\d+)(?:/L(\d+))?\s*-\s*(.*)', parts.group(2))
                    if activity_parts:
                        activity = f"L{activity_parts.group(1)}"
                        if activity_parts.group(2):
                            activity += f"/L{activity_parts.group(2)}"
                        description = activity_parts.group(3)
                    else:
                        raise ValueError(
                            f"Invalid activity format in line {i+1}")
                else:
                    activity = ""
                    description = ""
                self.activities.append((date, activity, description))
            else:
                raise ValueError(f"Invalid line format in line {i+1}")

    def __str__(self):
        output = ""
        for date, activity, description in self.activities:
            output += f"{date}: {activity} - {description}\n"
        return output
