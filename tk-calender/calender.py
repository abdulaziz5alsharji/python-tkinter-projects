try:
    from tkinter import *
    from PIL import ImageTk, Image
    import calendar
    from tkinter import messagebox
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Press Any Key To Exit ....")
    sys.exit()


class Calender:
    def __init__(self):
        # Window Design
        self.root = Tk()
        self.root.geometry("400x300")
        self.root.title("Calender")
        self.root.resizable(0, 0)
        self.root.iconbitmap("calendar-icon.ico")

        # VARS
        self.month_var = IntVar()
        self.year_var = IntVar()

        # Label Image
        self.image = ImageTk.PhotoImage(Image.open("calendar.png"))
        self.label_image = Label(self.root, image=self.image)
        self.label_image.place(x=170, y=3)

        # Label (1)
        self.month_label = Label(self.root, text="Month", font=("verdana", 10, "bold"))
        self.month_label.place(x=70, y=80)

        # Label (2)
        self.year_label = Label(self.root, text="Year", font=("verdana", 10, "bold"))
        self.year_label.place(x=210, y=80)

        # Spin Box (1)
        self.year_spinbox = Spinbox(self.root, from_=2021, to=3000, width=8, textvariable=self.year_var)
        self.year_spinbox.place(x=260, y=80)

        # Spin Box (2)
        self.month_spinbox = Spinbox(self.root, from_=1, to=12, width=5, textvariable=self.month_var)
        self.month_spinbox.place(x=140, y=80)

        # Text
        self.result_text = Text(self.root, width=33, height=8, relief=RIDGE, borderwidth=2)
        self.result_text.place(x=70, y=110)

        # Button (1)
        self.clear_button = Button(self.root, text="Clear", command=self.clear, relief=RIDGE
                                   , borderwidth=2, font=("verdana", 10, "bold"))
        self.clear_button.place(x=200, y=250)

        # Button (2)
        self.show_button = Button(self.root, text="Show", command=self.show, relief=RIDGE
                                  , borderwidth=2, font=("verdana", 10, "bold"))
        self.show_button.place(x=140, y=250)

        # Button (3)
        self.exit_button = Button(self.root, text="Exit", command=self.exit, relief=RIDGE
                                  , borderwidth=2, font=("verdana", 10, "bold"))
        self.exit_button.place(x=260, y=250)

        # Window LOOP
        self.root.mainloop()

    # Clear Method
    def clear(self):
        self.result_text.delete(1.0, END)

    # Show Method
    def show(self):
        try:
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, calendar.month(self.year_var.get(), self.month_var.get()))
        except Exception:
            messagebox.showerror("Error", "Error")

    # Exit Method
    def exit(self):
        self.check = messagebox.askyesno("Exit", "Do You Want To Exit")
        if self.check:
            self.root.destroy()
        else:
            pass


if __name__ == "__main__":
    Calender()
