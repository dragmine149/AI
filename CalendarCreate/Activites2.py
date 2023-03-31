def activities(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    current_date = ''
    current_activities = ''

    for line in lines:
        if ' -- ' in line:  # handle dates
            current_date = line.split(' -- ')[0]
            current_activities = ''

        elif line.strip():  # handle activities
            current_activities += line.strip() + '\n'

        if current_date and current_activities:  # output activity for each day
            print(f"{current_date.strip()}\n{'='*len(current_date.strip())}")
            activities_list = current_activities.strip().split('\n')
            for activity in activities_list:
                label, desc = activity.split(' - ')
                print(f"{label.strip()} - {desc.strip()}")
            print()
            current_activities = ''


if __name__ == "__main__":
    activities('data.txt')
