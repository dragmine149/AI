from ActivityCalendar4 import ActivityCalendar
import datetime

if __name__ == '__main__':
    calendar = ActivityCalendar('data.txt')
    date_str = input("Enter date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_str, '%d/%m/%Y').date()
    activities = calendar.get_activities_for_date(date)
    print(f'Activities for {date.strftime("%d/%m/%Y")}:')
    print('=' * 7)
    for activity in activities:
        print(activity)
