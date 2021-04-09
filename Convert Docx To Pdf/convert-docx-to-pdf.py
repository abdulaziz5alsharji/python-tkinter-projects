import sys

try:
    from tkinter import *
    import docx2pdf
    from tkinter import messagebox
    from tkinter import filedialog
    import threading
except ModuleNotFoundError as error:
    print(error)
    input("Press Any Key To Exit .. ")
    sys.exit()


class DocxToPDF:
    def __init__(self) -> None:
        # Window Design
        self.root = Tk()
        self.root.title("DOCX2PDF")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        self.root.configure(bg="#FFF")
        self.root.iconbitmap("pdf-icon.ico")
        # Vars
        self.docx_var = StringVar()
        self.pdf_var = StringVar()
        # Title Label
        self.title_label = Label(self.root, text="Convert Docx To Pdf", bg="#FFF", font=("roboto", 20, "bold"))
        self.title_label.pack(fill="x", pady=20)
        # Entries
        docx_entry = Entry(self.root, width=35, highlightbackground="black", state="disabled",
                           highlightcolor="black", highlightthickness=2, textvariable=self.docx_var)
        docx_entry.place(x=30, y=120)

        pdf_entry = Entry(self.root, width=35, highlightbackground="black", state="disabled",
                          highlightcolor="black", highlightthickness=2, textvariable=self.pdf_var)
        pdf_entry.place(x=30, y=160)
        # Buttons
        docx_button = Button(self.root, text="Docx", width=10, borderwidth=2, bg="black"
                             , fg="white", font=("verdana", 10, "bold"), command=self.get_docx)
        docx_button.place(x=265, y=118)

        pdf_button = Button(self.root, text="Save", width=10, borderwidth=2, bg="black"
                            , fg="white", font=("verdana", 10, "bold"), command=self.save)
        pdf_button.place(x=265, y=158)

        convert_button = Button(self.root, text="Convert", width=10, borderwidth=2, bg="black"
                                , fg="white", font=("verdana", 10, "bold"), command=self.covert_thread)
        convert_button.place(x=150, y=220)

        clear_button = Button(self.root, text="Clear", width=10, borderwidth=2, bg="black"
                              , fg="white", font=("verdana", 10, "bold"), command=self.clear)
        clear_button.place(x=265, y=220)

        exit_button = Button(self.root, text="Exit", width=10, borderwidth=2, bg="black"
                             , fg="white", font=("verdana", 10, "bold"), command=self.exit_)
        exit_button.place(x=30, y=220)
        self.root.mainloop()

    def get_docx(self):
        self.docx_var.set(filedialog.askopenfilename())

    def save(self):
        self.pdf_var.set(filedialog.askdirectory())

    def convert(self):
        if self.docx_var.get() == "":
            messagebox.showerror("Error", "Choose Docx File")
        elif self.pdf_var.get() == "":
            messagebox.showerror("Error", "Choose Path")
        else:
            try:
                docx2pdf.convert(self.docx_var.get(), f"{self.pdf_var.get()}/0001.pdf")
                messagebox.showinfo("Converted", "Done")
            except Exception:
                messagebox.showerror("Error", "Error")

    def covert_thread(self):
        threading.Thread(target=self.convert).start()

    def clear(self):
        self.pdf_var.set("")
        self.docx_var.set("")

    def exit_(self):
        check = messagebox.askyesno("Exit", "Do you want to exit ?")
        if check:
            self.root.destroy()
        else:
            pass


if __name__ == '__main__':
    DocxToPDF()
