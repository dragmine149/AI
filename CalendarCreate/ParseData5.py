import datetime


def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    current_date = None
    current_label = None
    current_activities = []

    # Loop through lines in file
    for line in lines:
        line = line.strip()
        if not line:
            # Skip empty lines
            continue
        if line.count('/') == 2:
            # Line contains date
            current_date = datetime.datetime.strptime(line, '%d/%m/%y').date()
            print(current_date.strftime('%d/%m/%y'))
            print('=' * 7)
            current_label = None
            current_activities = []
        elif line.startswith('L'):
            # Line contains label and activity
            label, activity = line.split('-', maxsplit=1)
            label = label.strip()
            activity = activity.strip()
            if label != current_label:
                # New label, print previous activities and update label
                if current_label is not None:
                    print('\n'.join(current_activities))
                    print()
                current_label = label
                current_activities = []
            current_activities.append(f'{label} - {activity}')
        elif '--' in line:
            # Line contains extra information
            line, extra_info = line.split('--', maxsplit=1)
            line = line.strip()
            extra_info = extra_info.strip()
            label, activity = line.split('-', maxsplit=1)
            label = label.strip()
            activity = activity.strip()
            if label != current_label:
                # New label, print previous activities and update label
                if current_label is not None:
                    print('\n'.join(current_activities))
                    print()
                current_label = label
                current_activities = []
            current_activities.append(f'{label} - {activity} -- {extra_info}')

    # Print last activities
    if current_label is not None:
        print('\n'.join(current_activities))
        print()


if __name__ == "__main__":
    parse_data('data.txt')
