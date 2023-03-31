class Activities:
    def __init__(self, filename):
        self.events = []
        with open(filename) as f:
            for line in f:
                parts = line.strip().split(' - ')
                if len(parts) == 2:
                    self.events.append({'date': parts[0], 'text': [parts[1]]})
                elif len(self.events) > 0:
                    self.events[-1]['text'].append(line.strip())

    def print_calendar(self):
        for event in self.events:
            print(event['date'])
            for i, text in enumerate(event['text'], start=1):
                print(f"L{i} - {text}")
            print()


if __name__ == '__main__':
    activities = Activities('data.txt')
    activities.print_calendar()
