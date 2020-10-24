import tkinter as tk

from time_tracker import TimeTracker


def convert_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return minutes, seconds


class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('Time Tracker')
        self.tracker = TimeTracker()
        self.timer_labels = []

        self.input_frame = tk.Frame(self.master)
        self.create_button = tk.Button(self.input_frame, text='Create', command=self.create_timer)
        self.name_bar = tk.Entry(self.input_frame)

        self.create_input_widgets()
        self.update_clock()

    def create_input_widgets(self):
        self.input_frame.pack()
        self.name_bar.pack(side='right')
        self.create_button.pack(side='right')

    def create_timer(self):
        if self.name_bar.get().strip() == '':
            return

        timer_frame = tk.Frame(self.master)
        timer_name = self.name_bar.get()
        self.tracker.create(timer_name)
        label_name = tk.Label(timer_frame, text=timer_name)
        label_value = tk.Label(timer_frame, text=f'0 min 0 sec')
        start_button = tk.Button(timer_frame, text='Start', command=lambda: self.start(timer_name))
        stop_button = tk.Button(timer_frame, text='Stop', command=lambda: self.stop(timer_name))

        self.timer_labels.append([label_value, timer_name])

        self.name_bar.delete(0, tk.END)
        timer_frame.pack(fill='x')
        start_button.pack(side='left')
        stop_button.pack(side='left')
        label_name.pack(side='left')
        label_value.pack(side='right')

    def start(self, timer):
        if self.tracker.active_trackers[timer].stopped is True:
            self.tracker.active_trackers[timer].start()

    def stop(self, timer):
        if self.tracker.active_trackers[timer].stopped is False:
            self.tracker.active_trackers[timer].stop()

    def update_clock(self):
        for values in self.timer_labels:
            minutes, seconds = convert_time(self.tracker.active_trackers[values[1]].read())
            values[0].configure(text=f'{minutes} min {seconds} sec')
        self.master.after(500, self.update_clock)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
