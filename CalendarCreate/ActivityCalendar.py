import datetime


class ActivityCalendar:
    def __init__(self, filename):
        self.data = {}
        self.load_data(filename)

    def load_data(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        current_date = None
        for line in lines:
            if line.startswith('\n'):
                current_date = None
            elif not current_date:
                current_date = datetime.datetime.strptime(
                    line.strip(), '%d/%m/%y').date()
                self.data[current_date] = []
            else:
                if '--' in line:
                    line_parts = line.split('--')
                    activity = line_parts[0].strip()
                    extra_info = line_parts[1].strip()
                    self.data[current_date].append((activity, extra_info))
                else:
                    self.data[current_date].append((line.strip(), None))

    def get_activities(self, date):
        activities = self.data.get(date, [])
        return activities


if __name__ == '__main__':
    calendar = ActivityCalendar('data.txt')
    date = datetime.date(2022, 1, 1)
    print(f"Activities for {date.strftime('%d/%m/%y')}:")
    print(calendar.get_activities(date))
