try:
    from tkinter import *
    from tkinter import messagebox
    from PIL import ImageTk, Image
    from datetime import datetime
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Press to Exit ..")
    sys.exit()


class SystemLogin:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x500")
        self.root.title("System Login")
        self.root.resizable(0, 0)
        self.root.iconbitmap(r"login-icon.ico")
        # Vars
        self.user_var = StringVar()
        self.password_var = StringVar()
        # Frame
        self.full_frame = Frame(self.root, width=400, height=500, relief=RIDGE, borderwidth=5, bg="#1695e0")
        self.full_frame.pack()
        self.image = ImageTk.PhotoImage(Image.open(r"login-image.png"))
        self.image_label = Label(self.root, image=self.image, bg="#1695e0")
        self.image_label.place(x=160, y=25)
        # Label Frame
        self.login_label_frame = LabelFrame(self.full_frame, text="LOGIN",
                                            bg="#1695e0", width=390, height=400
                                            , relief=RIDGE, borderwidth=3, font=('verdana', 14, 'bold'), border=4)
        self.login_label_frame.place(x=0, y=90)
        # Labels
        self.user_label = Label(self.login_label_frame, text="Username:", bg="#1695e0", font=('verdana', 12, 'bold'))
        self.user_label.place(x=4, y=30)

        self.pass_label = Label(self.login_label_frame, text="Password:", bg="#1695e0", font=('verdana', 12, 'bold'))
        self.pass_label.place(x=4, y=100)

        self.date_label = Label(self.full_frame, text=datetime.now().date(),
                                bg="#1695e0", font=('verdana', 10, 'bold'))
        self.date_label.place(x=0, y=0)

        self.title_label = Label(self.full_frame, text="Login System",
                                 bg="#1695e0", font=('verdana', 11, 'bold'))
        self.title_label.place(x=130, y=0)

        self.footer_label = Label(self.login_label_frame, text="Coding By Insta:@5AB_F $$CopyRight",
                                  bg="#1695e0", font=('verdana', 11, 'bold'))
        self.footer_label.place(x=30, y=340)
        # Entries
        self.user_entry = Entry(self.login_label_frame,
                                width=30, relief=RIDGE, borderwidth=3,
                                highlightbackground="#1695e0",
                                highlightcolor="#1695e0", highlightthickness=2,
                                font=('verdana', 10, 'bold'), textvariable=self.user_var)
        self.user_entry.place(x=4, y=60)

        self.pass_entry = Entry(self.login_label_frame,
                                width=30, relief=RIDGE, borderwidth=3,
                                highlightbackground="#1695e0",
                                highlightcolor="#1695e0", highlightthickness=2,
                                font=('verdana', 10, 'bold'), textvariable=self.password_var, show="*")
        self.pass_entry.place(x=4, y=130)
        # Buttons
        self.login_button = Button(self.login_label_frame, text="Login",
                                   font=('verdana', 10, 'bold'), width=10,
                                   relief=RAISED, borderwidth=2, bg="white", command=self.login)
        self.login_button.place(x=4, y=170)
        self.clear_button = Button(self.login_label_frame, text="Reset",
                                   font=('verdana', 8, 'bold'), width=8,
                                   relief=RAISED, borderwidth=2, bg="white", command=self.clear)
        self.clear_button.place(x=200, y=170)
        self.exit_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Dell\Desktop\image_tk\logout_image.png"))
        self.exit_button = Button(self.full_frame, image=self.exit_image,
                                  font=('verdana', 8, 'bold'), width=20, height=20,
                                  relief=RAISED, borderwidth=2, bg="#1695e0"
                                  , command=self.logout)
        self.exit_button.place(x=362, y=0)
        self.root.mainloop()

    def login(self):
        if self.password_var.get() == "" and self.user_var.get() == "":
            messagebox.showerror("Login Error", "Fill The Form Plz")
        elif self.password_var.get() == "admin" and self.user_var.get() == "root":
            messagebox.showinfo("Login Done", "Welcome In Your Account")
        else:
            messagebox.showerror("Login Error", "Check Your Password or Username")

    def clear(self):
        self.password_var.set("")
        self.user_var.set("")

    def logout(self):
        check = messagebox.askyesno("Exit Program", "Do You Want To Exit ??")
        if check:
            self.root.destroy()


if __name__ == "__main__":
    SystemLogin()
