import datetime


def parse_data(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    # Initialize the date to None
    date = None

    for line in lines:
        # Check if the line contains a date in the format dd/mm/yy
        try:
            date = datetime.datetime.strptime(line.strip(), '%d/%m/%y').date()
            continue
        except ValueError:
            pass

        # If the line doesn't contain a date, print the label and activity
        if date is not None and line.strip():
            print(f'{date.strftime("%d/%m/%y")}\n{"="*7}')
            print(line.strip())


if __name__ == '__main__':
    parse_data('data.txt')
