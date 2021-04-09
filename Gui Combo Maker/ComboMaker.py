import threading
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class GuiComboMaker:
    def __init__(self):
        # Window Design
        self.root = Tk()
        self.root.geometry("250x330")
        self.root.resizable(0, 0)
        self.root.title("Combo Maker")
        self.root.configure(bg="#FFF")
        self.root.iconbitmap("combo-icon.ico")
        # Global Variables
        self.list_users = list()
        self.list_passwords = list()
        self.save_path = ""
        # Users Button
        self.users_button = Button(self.root, text="Users", width=10, borderwidth=2, bg="black"
                                   , fg="white", font=("verdana", 10, "bold"), command=self.users)
        self.users_button.pack(fill="x")
        # Passwords Button
        self.passwords_button = Button(self.root, text="Passwords", width=10, borderwidth=2, bg="blue"
                                       , fg="white", font=("verdana", 10, "bold"), command=self.password)
        self.passwords_button.pack(fill="x")
        # Text
        self.text = Text(self.root, height=13, highlightbackground="black",
                         highlightcolor="black", highlightthickness=4)
        self.text.pack()
        # Save Button
        self.save_button = Button(self.root, text="Save", width=10, borderwidth=2, bg="black"
                                  , fg="white", font=("verdana", 10, "bold"), command=self.save)
        self.save_button.pack(fill="x")
        # Start Button
        self.start_button = Button(self.root, text="Start", width=10, borderwidth=2, bg="blue"
                                   , fg="white", font=("verdana", 10, "bold"), command=self.start_thread)
        self.start_button.pack(fill="x", side="bottom")

        self.root.mainloop()

    def save(self):
        Path = filedialog.askdirectory()
        if Path == "":
            pass
        else:
            self.save_path = f"{Path}/combo.txt"

    def users(self):
        file = filedialog.askopenfilename()
        if file == "":
            pass
        else:
            USERS = open(file, "r")
            self.list_users = USERS.read().split()
            USERS.close()

    def password(self):
        file = filedialog.askopenfilename()
        if file == "":
            pass
        else:
            PASS = open(file, "r")
            self.list_passwords = PASS.read().split()
            PASS.close()

    def start(self):
        if len(self.list_users) == 0 or len(self.list_passwords) == 0:
            messagebox.showerror("Error", "Users or Password Is Emtpy")
        elif self.save_path == "":
            messagebox.showerror("Error", "Choose Path To Save File")
        else:
            for user in self.list_users:
                for password in self.list_passwords:
                    with open(self.save_path, "a") as combo:
                        combo.write(f"{user}:{password}" + "\n")
                    self.text.insert(END, f"{user}:{password}\n")
            messagebox.showinfo("Done", "Done")

    def start_thread(self):
        threading.Thread(target=self.start).start()


if __name__ == '__main__':
    GuiComboMaker()
