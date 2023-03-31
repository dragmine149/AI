from calendar3 import Activities

activities = Activities('data.txt')
for activity in activities.activities:
    print(activity.date)
    print(activity.label)
    print(activity.description)
    print()
