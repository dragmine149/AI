import datetime


class ActivityCalendar:
    def __init__(self, filename):
        """
        Initialize an ActivityCalendar object with data from a file.

        Args:
        filename (str): The name of the file to read the data from.
        """
        self.data = {}
        self.load_data(filename)

    def load_data(self, filename):
        """
        Load data from a text file into the `data` dictionary.

        The text file should contain a list of activities with their corresponding dates
        in the following format:

        DD/MM/YY -- activity 1
        DD/MM/YY -- activity 2
        ...

        Empty lines indicate that there are no activities for the preceding date.
        Dates and activities are separated by two dashes (--).

        Parameters:
            filename (str): The name of the text file to load data from.

        Raises:
            ValueError: If the date in the text file is not in the correct format (DD/MM/YY).

        Returns:
            None.
        """
        with open(filename) as f:
            lines = f.readlines()
        current_date = None
        for line in lines:
            line = line.strip()
            if line == "":
                current_date = None
            elif current_date is None:
                try:
                    current_date = datetime.datetime.strptime(
                        line.split(" --")[0], '%d/%m/%y').date()
                except ValueError:
                    raise ValueError(
                        f"Invalid date format: {line.split(' --')[0]}. Use DD/MM/YY")
                self.data[current_date] = []
            else:
                self.data[current_date].append(line)

    def get_activities_for_date(self, date):
        """
        Retrieve the activities for a given date.

        Args:
        date (datetime.date): The date to retrieve activities for.

        Returns:
        A list of strings representing the activities for the given date.
        """
        activities = self.data.get(date, [])
        return activities


if __name__ == '__main__':
    calendar = ActivityCalendar('data.txt')
    date = datetime.date(2023, 3, 1)
    activities = calendar.get_activities_for_date(date)
    print(f'Activities for {date.strftime("%d/%m/%y")}:')
    print('=' * 7)
    for activity in activities:
        print(activity)
