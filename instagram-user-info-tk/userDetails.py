try:
    from tkinter import *
    import requests
    import threading
    from tkinter import messagebox
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter To Exit ...")
    sys.exit()


class InstagramInfo:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram User Details")
        self.root.geometry("400x300")
        self.root.resizable(0, 0)
        self.root.iconbitmap(r"instagram.ico")
        self.user_var = StringVar()
        # Frames
        self.full_frame = Frame(self.root, width=400, height=300, relief=RIDGE, borderwidth=5, bg="#248aa2")
        self.full_frame.pack()

        self.inner_frame = LabelFrame(self.full_frame, width=380, height=50,
                                      bg="#248aa2", relief=RIDGE, borderwidth=3,
                                      highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.inner_frame.place(x=5, y=5)
        # Form
        # User Entry
        self.user_entry = Entry(self.full_frame, width=30, relief=RIDGE, borderwidth=3, textvariable=self.user_var)
        self.user_entry.place(x=70, y=15)
        # Search Button
        self.search_button = Button(self.full_frame, text="Search", relief=RAISED, borderwidth=2,
                                    font=('verdana', 8, 'bold'), bg='#248aa2', fg="white", command=self.search_thread)
        self.search_button.place(x=270, y=15)

        # LabelFrames
        self.design_label_frame = LabelFrame(self.full_frame, width=380, height=240, relief=RIDGE,
                                             borderwidth=3, bg='#248aa2', highlightbackground="white"
                                             , highlightcolor="white", highlightthickness=2)
        self.design_label_frame.place(x=5, y=45)

        self.user_details_label_frame = LabelFrame(self.design_label_frame, text="Users Details", width=370,
                                                   height=230, highlightbackground="white",
                                                   highlightcolor="white", highlightthickness=5
                                                   , font=('verdana', 10, 'bold'))
        self.user_details_label_frame.place(x=0, y=0)

        # Details Text
        self.text_details = Text(self.user_details_label_frame,
                                 height=12, width=47, relief=RIDGE
                                 , borderwidth=5, highlightbackground="white"
                                 , highlightcolor="white", font=('courier', 9, ''))
        self.text_details.place(x=5, y=5)

    def search(self):
        try:
            target = self.user_var.get()
            if target == "":
                messagebox.showerror("Error", "Please Fill The Blank")
            else:
                session = requests.Session()
                url = f"https://www.instagram.com/{target}/?__a=1"
                headers = {
                    'HOST': "www.instagram.com",
                    'KeepAlive': 'True',
                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
                    'Cookie': 'cookie',
                    'Accept': "*/*",
                    'ContentType': "application/x-www-form-urlencoded",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-IG-App-ID": "936619743392459",
                    "X-Instagram-AJAX": "missing",
                    "X-CSRFToken": "missing",
                    "Accept-Language": "en-US,en;q=0.9"
                }
                req = session.get(url, headers=headers).json()
                bio = req['graphql']['user']['biography']
                link = req['graphql']['user']['external_url']
                name = req['graphql']['user']['full_name']
                idd = req['graphql']['user']['id']
                profile_photo = req['graphql']['user']['profile_pic_url']

                details = f"user>>{target}\nname>>{name}\nid>>{idd}\nlink>>{link}\nbiography>>{bio}\nprofile photo>>{profile_photo} "
                self.text_details.insert(END, details)
        except Exception as error:
            print(error)
            messagebox.showerror("User Error", "Please Type Correct User")

    def search_thread(self):
        thread = threading.Thread(target=self.search)
        thread.start()


if __name__ == "__main__":
    Root = Tk()
    InstagramInfo(root=Root)
    Root.mainloop()
