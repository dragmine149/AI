import datetime


def parse_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    current_date = None
    output = ''
    for line in lines:
        if line.startswith('--'):
            # Ignore lines that start with '--'
            continue
        if line.startswith('L'):
            if not current_date:
                # If there is no current date, set it to today
                current_date = datetime.date.today()
            label, activity = line.strip().split(' - ')
            output += '{}\n=======\n{} - {}\n'.format(
                current_date.strftime('%d/%m/%y'), label, activity)
        elif line.strip() == '':
            # Ignore blank lines
            continue
        else:
            try:
                # Attempt to create a new date from the line
                current_date = datetime.datetime.strptime(
                    line.strip().split('--')[0], '%d/%m/%y').date()
            except ValueError:
                # If the line cannot be converted to a date, ignore it
                continue
    return output


if __name__ == "__main__":
    print(parse_data('data.txt'))
