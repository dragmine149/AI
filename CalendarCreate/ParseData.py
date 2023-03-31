from datetime import datetime


def parse_data(file):
    # Read lines from file
    with open(file, 'r') as f:
        lines = f.readlines()

    # Initialize variables
    current_date = None
    activities = {}

    # Iterate over lines and group activities by date
    for line in lines:
        # Parse date from line
        try:
            date = datetime.strptime(line.strip(), '%d/%m/%y')
            current_date = date.strftime('%d/%m/%y')
            activities[current_date] = []
        except ValueError:
            pass

        # Parse activity from line
        if current_date is not None and '-' in line:
            label, activity = line.strip().split('-', 1)
            activities[current_date].append((label.strip(), activity.strip()))

    # Format output
    output = []
    for date, activities_list in activities.items():
        output.append(date)
        output.append('=' * len(date))
        for i, (label, activity) in enumerate(activities_list, 1):
            output.append(f"L{i} - {label} - {activity}")
        output.append('')

    return '\n'.join(output)


if __name__ == "__main__":
    r = parse_data('data.txt')
    print(r)
