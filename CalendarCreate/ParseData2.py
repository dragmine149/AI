import datetime


def parse_data(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        date = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if '/' in line:
                date = datetime.datetime.strptime(line, '%d/%m/%y')
            else:
                line_label, line_desc = line.split(' - ')
                label = line_label[2:]
                print(date.strftime('%d/%m/%y'))
                print('=' * len(date.strftime('%d/%m/%y')))
                print(f"{label} - {line_desc}")


if __name__ == "__main__":
    parse_data('data.txt')
