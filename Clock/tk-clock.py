from tkinter import *
from time import strftime


class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.root.resizable(0, 0)
        self.root.iconbitmap("clock-icon.ico")
        # VARS
        self.time_var = StringVar()
        # Time Label
        self.time_label = Label(self.root, bg="black", fg="cyan", font=("ds-digital", 80, "bold"),
                                textvariable=self.time_var)
        self.time_label.pack()
        self.Time()

    def Time(self):
        time = strftime("%I:%M:%S %p")
        self.time_var.set(time)
        self.time_label.after(1000, self.Time)


if __name__ == '__main__':
    ROOT = Tk()
    clock = Clock(ROOT)
    ROOT.mainloop()
