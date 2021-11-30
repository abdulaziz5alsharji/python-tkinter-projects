import threading
import time
import random
from tkinter import *


class SpeedTypingTest:
    def __init__(self):
        self.root = Tk()
        self.root.title("Speed Typing Test")
        self.root.geometry("600x400")
        self.root.resizable(0, 0)
        # Text Label
        self.file = open("speedTypingText.txt", "r")
        self.text_list = self.file.read().split("\n")
        self.text_label = Label(self.root, text=random.choice(self.text_list), font=("Helvetica", 14))
        self.text_label.place(x=20, y=40)

        # Entry
        self.entry = Entry(self.root, font=("Helvetica", 15))
        self.entry.pack(fill="x", padx=10, pady=100)
        self.entry.bind("<KeyRelease>", self.start)
        # Speed Label
        self.speed_label = Label(self.root, text="Speed: \n0.00 CPS\n0.00 CPM", font=("Helvetica", 15))
        self.speed_label.place(x=250, y=150)

        # Paused Button
        self.restart_button = Button(self.root, text="Restart", font=("Helvetica", 13), command=self.restart)
        self.restart_button.place(x=260, y=250)

        self.counter = 0
        self.running = False

        self.root.mainloop()

    def start(self, event):
        if not self.running and event.keycode not in [16, 17, 18]:
            self.running = True
            thread = threading.Thread(target=self.timing_speed)
            thread.start()
        if not self.text_label.cget("text").startswith(self.entry.get()):
            self.entry.configure(fg="red")
        else:
            self.entry.configure(fg="black")
        if self.text_label.cget("text") == self.entry.get():
            self.running = False
            self.entry.configure(fg="green")

    def timing_speed(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.entry.get()) / self.counter
            cpm = cps * 60
            self.speed_label.configure(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM")
            self.root.update()

    def restart(self):
        self.counter = 0
        self.running = False
        self.text_label.configure(text=random.choice(self.text_list))
        self.speed_label.configure(text="Speed: \n0.00 CPS\n0.00 CPM")
        self.entry.delete(0, END)


if __name__ == '__main__':
    SpeedTypingTest()
