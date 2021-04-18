import sys

try:
    from tkinter import *
    from tkinter import filedialog
    from tkinter import messagebox
    from tkinter.scrolledtext import ScrolledText
    import subprocess
    import threading
except ModuleNotFoundError as er:
    print(er)
    input("Press Any Key To Exit ..")
    sys.exit()


class IDE:
    def __init__(self):
        # Window Design
        self.root = Tk()
        self.root.title("PYTHON IDE")
        self.root.geometry("1750x1750")
        self.root.iconbitmap("IDE-icon.ico")
        # Code Text
        self.file_path = ""
        self.code_text = ScrolledText(self.root, font=("roboto", 12, "bold"))
        self.code_text.pack(expand=True, fill="x", side="top")
        # Output Text
        self.output_text = ScrolledText(self.root, font=("roboto", 12, "bold"))
        self.output_text.pack(expand=True, fill="x", side="bottom")
        # Main Menu
        self.main_menu = Menu(self.root, font=("times new roman", 15, "bold"), activebackground="skyblue")
        self.root.config(menu=self.main_menu)
        # File Menu
        self.file_menu = Menu(self.main_menu, font=("times new roman", 12, "bold"), activebackground="skyblue",
                              tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open)
        self.file_menu.add_command(label="Save", command=self.save)
        self.file_menu.add_command(label="Save As", command=self.save_as)
        self.file_menu.add_command(label="Exit", command=self.exit_)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        # Run Menu
        self.run_menu = Menu(self.main_menu, font=("times new roman", 12, "bold"), activebackground="skyblue",
                             tearoff=0)
        self.run_menu.add_command(label="Run", command=self.thread_run)
        self.main_menu.add_cascade(label="Run", menu=self.run_menu)
        self.root.mainloop()

    def run(self):
        if self.file_path == "":
            messagebox.showerror("Error", "You should save file")
        else:
            command = f"python {self.file_path}"
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            self.output_text.delete(1.0, END)
            self.output_text.insert(END, output)
            self.output_text.insert(END, error)

    def thread_run(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def set_file_path(self, path):
        self.file_path = path

    def open(self):
        path = filedialog.askopenfilename(filetype=[("Python Files", "*.py")])
        if path == "":
            messagebox.showerror("Error", "You should open file")
        else:
            with open(path, "r") as file:
                self.code_text.delete(1.0, END)
                self.code_text.insert(END, file.read())
                self.set_file_path(path)

    def save(self):
        if self.file_path == "":
            path = filedialog.asksaveasfilename(filetype=[("Python Files", "*.py")])
            if path == "":
                messagebox.showerror("Error", "You should save file")
                return
        else:
            path = self.file_path
        with open(path, "w") as file:
            code = self.code_text.get(1.0, END)
            file.write(code)
            self.set_file_path(path)

    def save_as(self):
        if self.file_path == "":
            path = filedialog.asksaveasfilename(filetype=[("Python Files", "*.py")])
            if path == "":
                messagebox.showerror("Error", "You should save file")
                return
        else:
            path = self.file_path
        with open(path, "w") as file:
            code = self.code_text.get(1.0, END)
            file.write(code)
            self.set_file_path(path)

    def exit_(self):
        check = messagebox.askyesno("Exit", "Do you want to exit?")
        if check:
            self.root.destroy()


if __name__ == '__main__':
    IDE()
