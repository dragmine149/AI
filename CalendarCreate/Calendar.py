import datetime


class Calendar:
    def __init__(self, filename):
        self.data = {}
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
                self.data[current_date].append(line.strip())

    def get_activities_for_date(self, date):
        return self.data.get(date)

    def get_all_activities(self):
        return self.data


if __name__ == "__main__":
    calendar = Calendar('data.txt')
    date = datetime.date(2023, 3, 30)
    activities = calendar.get_activities_for_date(date)
    print(activities)
    all_activities = calendar.get_all_activities()
    print(all_activities)
