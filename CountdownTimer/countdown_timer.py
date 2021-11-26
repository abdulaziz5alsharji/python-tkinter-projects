from tkinter import *
from tkinter import messagebox
from time import sleep
import threading
from win10toast import ToastNotifier


class App:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Countdown Timer")
        self.root.resizable(0, 0)
        self.root.geometry("460x220")
        # VARS
        self.FONT = ("Helvetica", 20)
        # Entry
        self.entry = Entry(self.root, font=self.FONT)
        self.entry.pack(fill="x", padx=5, pady=5)
        # Buttons
        self.start_button = Button(self.root, text="Start", font=self.FONT, command=self.start_thread)
        self.start_button.place(x=70, y=50)

        self.stop_button = Button(self.root, text="Stop", font=self.FONT, command=self.stop)
        self.stop_button.place(x=300, y=50)

        # Labels
        self.time_label = Label(self.root, text="Time: 00:00:00", font=self.FONT)
        self.time_label.place(x=120, y=130)

        self.is_stop = False
        self.root.mainloop()

    def start(self) -> None:
        hours, minutes, seconds = 0, 0, 0

        time = list(map(int, str(self.entry.get()).split(":")))
        if len(time) == 3:
            hours = time[0]
            minutes = time[1]
            seconds = time[2]
        elif len(time) == 2:
            hours = time[0]
            minutes = time[1]
        elif len(time) == 1:
            hours = time[0]
        else:
            messagebox.showerror("Error", "Time Format Error")
            return

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.is_stop:
            full_seconds -= 1
            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.configure(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            sleep(1)

        if not self.is_stop:
            notification = ToastNotifier()
            notification.show_toast("CountDown Timer", "Time Is Up!", duration=10)
        else:
            self.is_stop = False
            return

    def start_thread(self):
        thread = threading.Thread(target=self.start)
        thread.start()

    def stop(self) -> None:
        self.is_stop = True
        self.time_label.configure(text="Time: 00:00:00")


if __name__ == '__main__':
    App()
