import datetime


def parse_data(filename):
    with open(filename) as f:
        lines = f.readlines()
    data = {}
    current_date = None
    for line in lines:
        line = line.strip()
        if not line:
            current_date = None
        elif not current_date:
            date_str = line.split('--')[0].strip()
            current_date = datetime.datetime.strptime(
                date_str, '%d/%m/%y').date()
            data[current_date] = []
            if '--' in line:
                activity = line.split('--')[1].strip()
                data[current_date].append(activity)
        else:
            if '--' in line:
                activity = line.split('--')[1].strip()
                data[current_date].append(activity)
            else:
                data[current_date].append(line)
    for date, activities in data.items():
        print(date.strftime('%d/%m/%y'))
        print('=' * 7)
        for activity in activities:
            print(activity)



if __name__ == '__main__':
    parse_data('data.txt')
