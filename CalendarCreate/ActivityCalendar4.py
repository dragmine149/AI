import datetime
from typing import Dict, List


class ActivityCalendar:
    def __init__(self, filename: str) -> None:
        """
        Initialize a new ActivityCalendar object with data from the given file.

        Args:
        - filename (str): The name of the file to load data from.

        Returns:
        None
        """
        self.data: Dict[datetime.date, List[str]] = {}
        self.load_data(filename)

    def load_data(self, filename: str) -> None:
        """
        Load data from the given file into the ActivityCalendar object.

        Args:
        - filename (str): The name of the file to load data from.

        Returns:
        None
        """
        with open(filename) as f:
            lines = f.readlines()
        current_date: datetime.date = None
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

    def get_activities_for_date(self, date: datetime.date) -> List[str]:
        """
        Retrieve the activities for the specified date.

        Args:
        - date (datetime.date): The date to retrieve activities for.

        Returns:
        A list of strings representing the activities for the specified date.
        """
        activities: List[str] = self.data.get(date, [])
        return activities
