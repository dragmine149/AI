import datetime


def parse_data(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = {}
    current_date = None
    for line in lines:
        if line.startswith('\n'):
            current_date = None
        elif not current_date:
            current_date = datetime.datetime.strptime(
                line.strip(), '%d/%m/%y').date()
            data[current_date] = []
        else:
            data[current_date].append(line.strip())
    for date, activities in data.items():
        print(date.strftime('%d/%m/%y'))
        print('=' * 7)
        for activity in activities:
            print(activity)


if __name__ == '__main__':
    parse_data('data.txt')
