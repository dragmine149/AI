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
            line = line.strip()
            if line == "":
                current_date = None
            elif current_date is None:
                current_date = datetime.datetime.strptime(
                    line.split(" --")[0], '%d/%m/%y').date()
                self.data[current_date] = []
            else:
                self.data[current_date].append(line)

    def get_activities_for_date(self, date):
        activities = self.data.get(date)
        if activities:
            return activities
        else:
            return []


if __name__ == '__main__':
    calendar = ActivityCalendar('data.txt')
    date = datetime.date(2023, 3, 1)
    activities = calendar.get_activities_for_date(date)
    print(f'Activities for {date.strftime("%d/%m/%y")}:')
    print('=' * 7)
    for activity in activities:
        print(activity)
