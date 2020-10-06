import tkinter as tk
from time import time

from time_tracker import TimeTracker


class Application(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
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
        timer_frame = tk.Frame(self.master)
        timer_name = self.name_bar.get()
        self.tracker.create(timer_name)
        label_name = tk.Label(timer_frame, text=timer_name)
        label_value = tk.Label(timer_frame, text=0)
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
        self.tracker.tracking[timer].start()

    def stop(self, timer):
        self.tracker.tracking[timer].stop()

    def update_clock(self):
        for values in self.timer_labels:
            values[0].configure(text=self.tracker.tracking[values[1]].read())
        self.master.after(500, self.update_clock)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
