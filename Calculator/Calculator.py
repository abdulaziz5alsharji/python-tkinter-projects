try:
    from tkinter import *
    from tkinter import messagebox
except ModuleNotFoundError as error:
    import sys

    print(error)
    input("Press any key to exit ..")
    sys.exit()


class Calculator:
    def __init__(self):

        # Widow Design
        self.root = Tk()
        self.root.geometry("300x360")
        self.root.title("Calculator")
        self.root.iconbitmap(r"C:\Users\Dell\Desktop\icon\calculator-icon.ico")
        self.root.resizable(0, 0)

        # Var
        self.value_var = StringVar()

        # Entry
        self.value_entry = Entry(self.root, width=38, borderwidth=3,
                                 relief=RIDGE, textvariable=self.value_var)
        self.value_entry.grid(pady=10, row=0, sticky="w", padx=15)
        # Buttons

        self.button_0 = Button(self.root, text="0", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.zero)
        self.button_0.grid(row=4, sticky="w", padx=15, pady=5)

        self.button_00 = Button(self.root, text="00", borderwidth=3,
                                relief=RIDGE, width=5, height=2, command=self.double_zero)
        self.button_00.grid(row=4, sticky="w", padx=120, pady=5)

        self.button_1 = Button(self.root, text="1", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.one)
        self.button_1.grid(row=3, sticky="w", padx=120, pady=5)

        self.button_2 = Button(self.root, text="2", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.two)
        self.button_2.grid(row=3, sticky="w", padx=68, pady=5)

        self.button_3 = Button(self.root, text="3", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.three)
        self.button_3.grid(row=3, sticky="w", padx=15, pady=5)

        self.button_4 = Button(self.root, text="4", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.four)
        self.button_4.grid(row=2, sticky="w", padx=120, pady=5)

        self.button_5 = Button(self.root, text="5", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.five)
        self.button_5.grid(row=2, sticky="w", padx=68, pady=5)

        self.button_6 = Button(self.root, text="6", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.six)
        self.button_6.grid(row=2, sticky="w", padx=15, pady=5)

        self.button_7 = Button(self.root, text="7", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.seven)
        self.button_7.grid(row=1, sticky="w", padx=120)

        self.button_8 = Button(self.root, text="8", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.eight)
        self.button_8.grid(row=1, sticky="w", padx=68)

        self.button_9 = Button(self.root, text="9", borderwidth=3,
                               relief=RIDGE, width=5, height=2, command=self.nine)
        self.button_9.grid(row=1, sticky="w", padx=15)

        self.clear_button = Button(self.root, text="C", command=self.clear, bg="red",
                                   fg="white", relief=RIDGE, font=("verdana", 12, "bold"))
        self.clear_button.grid(row=0, sticky="w", padx=265, pady=15)

        self.button_dot = Button(self.root, text=".", borderwidth=3,
                                 relief=RIDGE, width=5, height=2, command=self.dot)
        self.button_dot.grid(row=4, sticky="w", padx=68, pady=5)

        self.button_result = Button(self.root, text="=", width=10, command=self.result, bg="red"
                                    , fg="white", borderwidth=3, relief=RIDGE, font=("verdana", 15, "bold"))
        self.button_result.grid(row=5, sticky="w", padx=15, pady=5)

        self.button_sum = Button(self.root, text="+", borderwidth=3,
                                 relief=RIDGE, width=5, height=2, command=self.sum)
        self.button_sum.grid(row=1, sticky="w", padx=240, pady=5)

        self.button_sub = Button(self.root, text="-", borderwidth=3,
                                 relief=RIDGE, width=5, height=2, command=self.sub)
        self.button_sub.grid(row=2, sticky="w", padx=240, pady=5)

        self.button_multiply = Button(self.root, text="x", borderwidth=3,
                                      relief=RIDGE, width=5, height=2, command=self.multiply)
        self.button_multiply.grid(row=3, sticky="w", padx=240, pady=5)

        self.button_divide = Button(self.root, text="÷", borderwidth=3,
                                    relief=RIDGE, width=5, height=2, command=self.divide)
        self.button_divide.grid(row=4, sticky="w", padx=240, pady=5)

        self.button_modulus = Button(self.root, text="%", borderwidth=3,
                                     relief=RIDGE, width=5, height=2, command=self.modulus)
        self.button_modulus.grid(row=5, sticky="w", padx=240, pady=5)

        # Widow Loop
        self.root.mainloop()

    def clear(self):
        self.value_var.set("")

    def result(self):
        try:
            if self.value_var.get() == "":
                messagebox.showerror("Error", "Error")
            else:
                self.result_ = eval(self.value_var.get())
                self.value_entry.insert(END, " = ")
                self.value_entry.insert(END, self.result_)
        except Exception:
            messagebox.showerror("Error", "Error")

    def zero(self):
        self.value_entry.insert(END, "0")

    def double_zero(self):
        self.value_entry.insert(END, "00")

    def one(self):
        self.value_entry.insert(END, "1")

    def two(self):
        self.value_entry.insert(END, "2")

    def three(self):
        self.value_entry.insert(END, "3")

    def four(self):
        self.value_entry.insert(END, "4")

    def five(self):
        self.value_entry.insert(END, "5")

    def six(self):
        self.value_entry.insert(END, "6")

    def seven(self):
        self.value_entry.insert(END, "7")

    def eight(self):
        self.value_entry.insert(END, "8")

    def nine(self):
        self.value_entry.insert(END, "9")

    def dot(self):
        self.value_entry.insert(END, ".")

    def sum(self):
        self.value_entry.insert(END, "+")

    def sub(self):
        self.value_entry.insert(END, "-")

    def divide(self):
        self.value_entry.insert(END, "/")

    def modulus(self):
        self.value_entry.insert(END, "%")

    def multiply(self):
        self.value_entry.insert(END, "*")


if __name__ == "__main__":
    Calculator()
