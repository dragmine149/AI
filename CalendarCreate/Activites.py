def Activities(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    date = ''
    for line in lines:
        if '-----' in line:
            date = ''
        elif '/' in line:
            date = line.strip()
        elif date and '-' in line:
            label, activity = line.strip().split('-', 1)
            print('='*5)
            print(date)
            print(f'{label.strip()} - {activity.strip()}')
            print('='*5)


if __name__ == "__main__":
    Activities('data.txt')
