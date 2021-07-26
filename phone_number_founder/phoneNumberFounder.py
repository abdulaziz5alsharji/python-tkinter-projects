import sys

try:
    import threading
    import requests
    from tkinter import *
    from tkinter import messagebox
    from tkinter.ttk import Combobox
    from datetime import datetime
except ModuleNotFoundError as error:
    print(error)
    sys.exit()


class PhoneNumberFounder:
    def __init__(self, window):
        self.root = window
        self.root.geometry("500x200")
        self.root.title("Phone Number Founder")
        self.root.resizable(0, 0)
        self.root.iconbitmap("phone_icon.ico")
        self.root.configure(bg="white")
        self.number = StringVar()
        self.name = StringVar()
        self.country = StringVar()
        self.countries = ["OM", "KW", "SA", "AE", "QA", "BH"]
        # Labels
        # Date Label
        self.date_label = Label(self.root, text=datetime.now().date(), fg="purple", font=("verdana", 10, "bold"))
        self.date_label.place(x=400, y=5)
        # Title Label
        self.title_label = Label(self.root, text="Phone Number Founder", fg="purple", bg="white",
                                 font=("verdana", 15, "bold"))
        self.title_label.place(x=90, y=5)
        # Caption Label
        self.caption_label = Label(self.root, text="Phone Number Here ..", fg="purple",
                                   font=("verdana", 10, "bold"))
        self.caption_label.place(x=50, y=50)
        # Countries Caption Label
        self.country_caption_label = Label(self.root, text="Countries Here ..", fg="purple",
                                           font=("verdana", 10, "bold"))
        self.country_caption_label.place(x=350, y=50)
        # Entry
        self.entry = Entry(self.root, textvariable=self.number, width=50, bg="lightgrey", relief=GROOVE, borderwidth=2,
                           border=2)
        self.entry.place(x=50, y=80)
        # Button
        self.button = Button(self.root, text="Find", bg="purple", fg="white",
                             font=("verdana", 8, "bold"), command=self.findThread, relief="groove")
        self.button.place(x=360, y=78)
        # Combobox
        self.country_combo_box = Combobox(self.root, textvariable=self.country, state="readonly",
                                          values=self.countries, width=5)
        self.country_combo_box.place(x=420, y=80)
        # Label Name
        self.label_name = Label(self.root, textvariable=self.name, fg="purple",
                                font=("verdana", 10, "bold"))
        self.label_name.place(x=165, y=125)

    def find(self):
        phoneNumber = self.number.get()
        country = self.country.get()
        if phoneNumber == "":
            messagebox.showerror("Error", "Please Enter The Number..")
        elif country == "":
            messagebox.showerror("Error", "Please Choose The Country..")
        elif phoneNumber == "" and country == "":
            messagebox.showerror("Error", "Please Choose The Country And Entry The Phone Number..")
        else:
            url = f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={phoneNumber}&country_code={country}"
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/87.0.4280.88 Safari/537.36"
            }
            response = requests.get(url, headers=headers).json()
            if response["msg"] == "Record found.":
                self.name.set(response["result"][0]["name"])
            else:
                self.name.set("[!!]NOT FOUND !!")

    def findThread(self):
        threading.Thread(target=self.find).start()


if __name__ == '__main__':
    root = Tk()
    PhoneNumberFounder(root)
    root.mainloop()
