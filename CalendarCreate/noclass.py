from datetime import datetime

# Define a function to convert date strings into datetime objects


def parse_date(date_str):
    return datetime.strptime(date_str, '%d/%m/%y')


# Define a dictionary to map day labels to integer values
day_map = {'L1': 0, 'L2': 1, 'L3': 2, 'L4': 3, 'L5': 4}

# Read data from file
with open('data.txt', 'r') as file:
    entries = []
    for line in file:
        parts = line.strip().split(' - ')
        date = parse_date(parts[0])
        day = parts[1]
        activity = parts[2]
        entries.append((date, day, activity))

# Sort entries by date
entries.sort()

# Create calendar
calendar = [[' ' for _ in range(5)] for _ in range(7)]
for entry in entries:
    date = entry[0]
    day = entry[1]
    activity = entry[2]
    row = date.day - 1
    col = day_map[day]
    calendar[row][col] = activity

# Print calendar
print('Monday Tuesday Wednesday Thursday Friday')
for row in range(7):
    for col in range(5):
        print(calendar[row][col], end='\t')
    print()
