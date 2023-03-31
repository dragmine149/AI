class Activity:
    def __init__(self, date, label, description):
        self.date = date
        self.label = label
        self.description = description


class Activities:
    def __init__(self, filename):
        self.activities = self.parse_data_file(filename)

    def parse_data_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        activities = []
        date = ''
        for line in lines:
            line = line.strip()
            if line:
                if '/' in line:
                    date = line
                else:
                    parts = line.split(' - ')
                    label = parts[0]
                    description = parts[1]
                    activities.append(Activity(date, label, description))
        return activities
