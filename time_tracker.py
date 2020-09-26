from time import time


class Tracker:

    def __init__(self):
        self.seconds = 0
        self.start_time = 0

    def start(self):
        self.start_time = time()

    def end(self):
        if self.seconds > 0:
            end = time()
            difference = end - self.start_time
            self.seconds += difference


class TimeTracker:

    def __init__(self):
        self.tracking = {}

    def __call__(self, name):
        if name in self.tracking:
            self.tracking[name] = Tracker()
            self.tracking[name].start()

    def get_all(self):
        for k, v in self.tracking.items():
            print(f'{k}: {round(v.finish(), 2)}')

if __name__ == '__main__':
    print('hello')