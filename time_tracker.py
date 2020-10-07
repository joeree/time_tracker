from time import time


class Tracker:

    def __init__(self):
        self.elapsed = 0
        self.start_time = 0
        self.stopped = True

    def start(self):
        self.stopped = False
        if self.elapsed == 0:
            self.start_time = time()
        else:
            self.start_time = time() - self.elapsed

    def stop(self):
        self.stopped = True
        difference = time() - self.start_time
        self.elapsed = int(difference)

    def read(self):
        if self.stopped:
            current = self.elapsed
        else:
            current = time() - self.start_time
        return int(current)


class TimeTracker:

    def __init__(self):
        self.trackers = {}

    def get_all(self):
        for k, v in self.trackers.items():
            print(f'{k}: {round(v.finish(), 2)}')

    def create(self, name):
        self.trackers[name] = Tracker()
