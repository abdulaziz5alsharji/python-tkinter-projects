from tkinter import *
from tkinter import messagebox


class ConversionApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Conversion App")
        self.root.resizable(0, 0)
        self.root.configure(bg="#9DBEBB")
        self.root.iconbitmap("conversion-icon.ico")
        # VARS
        self.number_var = IntVar()
        self.binary_var = IntVar()
        self.decimal_var = IntVar()
        self.hex_var = IntVar()
        self.oct_var = IntVar()
        # Title Label
        self.title_label = Label(self.root, text="Conversion System", font=('arial', 30), bg="#9DBEBB")
        self.title_label.pack(fill="x")
        # Number Entry
        self.number_entry = Entry(self.root, width=10, font=('times', 14), textvariable=self.number_var)
        self.number_entry.pack(pady=20)
        # Binary Entry
        self.binary_entry = Entry(self.root, width=10, state="readonly", font=('times', 14),
                                  textvariable=self.binary_var)
        self.binary_entry.pack(pady=10)
        # Decimal Entry
        self.decimal_entry = Entry(self.root, width=10, state="readonly", font=('times', 14),
                                   textvariable=self.decimal_var)
        self.decimal_entry.pack(pady=10)
        # Hex Entry
        self.hex_entry = Entry(self.root, width=10, state="readonly", font=('times', 14),
                               textvariable=self.hex_var)
        self.hex_entry.pack(pady=10)
        # Oct Entry
        self.oct_entry = Entry(self.root, width=10, state="readonly", font=('times', 14),
                               textvariable=self.oct_var)
        self.oct_entry.pack(pady=10)
        # Number Label
        self.number_label = Label(self.root, text="Enter A Number", bg="#9DBEBB", font=('times', 14))
        self.number_label.place(x=70, y=70)
        # Binary Label
        self.binary_label = Label(self.root, text="Binary", bg="#9DBEBB", font=('times', 14))
        self.binary_label.place(x=70, y=125)
        # Decimal Label
        self.decimal_label = Label(self.root, text="Decimal", bg="#9DBEBB", font=('times', 14))
        self.decimal_label.place(x=70, y=170)
        # Hex Label
        self.hex_label = Label(self.root, text="Hexadecimal", bg="#9DBEBB", font=('times', 14))
        self.hex_label.place(x=70, y=215)
        # Number Label
        self.oct_label = Label(self.root, text="Octal", bg="#9DBEBB", font=('times', 14))
        self.oct_label.place(x=70, y=260)
        # Converter Button
        self.convert_button = Button(self.root, text="Converter", command=self.convert, bg="#e20049",
                                     font=('times', 12), width=10)
        self.convert_button.place(x=100, y=310)
        # Clear Button
        self.convert_button = Button(self.root, text="Clear", command=self.clear, bg="light green",
                                     font=('times', 12), width=10)
        self.convert_button.place(x=210, y=310)
        # Exit Button
        self.exit_button = Button(self.root, text="Exit", command=self.exit_, bg="#e20049", font=('times', 12),
                                  width=10)
        self.exit_button.place(x=320, y=310)
        self.root.mainloop()

    def convert(self):
        try:
            if type(self.number_var.get()) == int or type(self.number_var.get()) == float:
                self.binary_var.set(bin(self.number_var.get()))
                self.decimal_var.set(round(self.number_var.get()))
                self.oct_var.set(oct(self.number_var.get()))
                self.hex_var.set(hex(self.number_var.get()))
            else:
                messagebox.showerror("Error!!", "Integer Or Float Number")
        except Exception as er:
            print(er)
            messagebox.showerror("Error!!", "Integer Or Float Number")

    def exit_(self):
        check = messagebox.askyesno("Exit", "Do you want to exit ??")
        if check:
            self.root.destroy()

    def clear(self):
        self.number_var.set("")
        self.binary_var.set("")
        self.decimal_var.set("")
        self.oct_var.set("")
        self.hex_var.set("")


if __name__ == '__main__':
    ConversionApp()
