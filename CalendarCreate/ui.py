import tkinter as tk
import datetime
from ActivityCalendar4 import ActivityCalendar


class CalendarUI:
    def __init__(self, calendar):
        self.calendar = calendar
        self.root = tk.Tk()
        self.root.title("Activity Calendar")

        self.label_date = tk.Label(self.root, text="Select a date:")
        self.label_date.pack()

        self.calendar_widget = tk.Calendar(self.root, selectmode='day',
                                           date_pattern='dd/MM/yyyy')
        self.calendar_widget.pack()

        self.button_show_activities = tk.Button(
            self.root, text="Show Activities", command=self.show_activities)
        self.button_show_activities.pack()

        self.text_activities = tk.Text(self.root)
        self.text_activities.pack()

        self.root.mainloop()

    def show_activities(self):
        selected_date = self.calendar_widget.selection_get().date()
        activities = self.calendar.get_activities_for_date(selected_date)
        self.text_activities.delete('1.0', tk.END)
        self.text_activities.insert(
            tk.END, f"Activities for {selected_date.strftime('%d/%m/%y')}:\n")
        self.text_activities.insert(tk.END, "=" * 7 + "\n")
        for activity in activities:
            self.text_activities.insert(tk.END, activity + "\n")


if __name__ == '__main__':
    calendar = ActivityCalendar('data.txt')
    app = CalendarUI(calendar)
