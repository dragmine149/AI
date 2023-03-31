from datetime import datetime

# Define a function to convert date strings into datetime objects


def parse_date(date_str):
    return datetime.strptime(date_str, '%d/%m/%y')


# Define a dictionary to map day labels to integer values
day_map = {'L1': 0, 'L2': 1, 'L3': 2, 'L4': 3, 'L5': 4}

# Define a class to represent the calendar


class Calendar:
    def __init__(self, entries):
        # Sort entries by date
        entries.sort()

        # Create empty calendar
        self.calendar = [[' ' for _ in range(5)] for _ in range(7)]

        # Fill in calendar with entries
        for entry in entries:
            date = entry[0]
            day = entry[1]
            activity = entry[2]
            row = date.day - 1
            col = day_map[day]
            self.calendar[row][col] = activity

    def __str__(self):
        # Generate string representation of calendar
        output = 'Monday Tuesday Wednesday Thursday Friday\n'
        for row in range(7):
            for col in range(5):
                output += self.calendar[row][col] + '\t'
            output += '\n'
        return output


# Read data from file
with open('data.txt', 'r') as file:
    entries = []
    for line in file:
        if not line.strip():  # skip empty lines
            continue
        parts = line.strip().split(' - ')
        date = parse_date(parts[0])
        day = parts[1]
        activity = parts[2]
        entries.append((date, day, activity))

# Create calendar
calendar = Calendar(entries)

# Print calendar
print(calendar)
