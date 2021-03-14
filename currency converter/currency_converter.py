try:
    from tkinter import *
    from tkinter.ttk import Combobox
    from datetime import datetime
    import requests
    from PIL import ImageTk, Image
    from tkinter import messagebox
    import threading
except ModuleNotFoundError as error:
    import sys
    print(error)
    input("Press to exit ..")
    sys.exit()

# Start Class
class CurrencyConverter:
    def __init__(self):

        # Window Design
        self.root=Tk()
        self.root.geometry("600x270")
        self.root.title("Currency Converter")
        self.root.resizable(0,0)
        self.root.iconbitmap(r"C:\Users\Dell\Desktop\icon\currency-converter-icon.ico")

        # VARS
        self.amount_var=IntVar()
        self.result_var=IntVar()
        self.currency_var=StringVar()
        self.usd_var=StringVar()
        self.currency_values=[
            'ALL',
            ' AFN',
            ' ARS',
            ' AWG',
            ' AUD',
            ' AZN',
            ' BSD',
            ' BBD',
            ' BYN',
            ' BZD	',
            ' BMD',
            ' BOB',
            'BAM',
            ' BWP',
            ' BGN',
            ' BND',
            ' KHR',
            ' CAD',
            ' KYD',
            ' CLP',
            ' CNY',
            ' COP		',
            ' CRC',
            ' HRK',
            'CUP',
            'CZK',
            ' DKK',
            ' DOP',
            ' XCD',
            ' EGP',
            ' SVC',
            ' EUR',
            ' FKP',
            ' FJD',
            ' GHS	',
            ' GIP',
            ' GTQ',
            'GGP',
            ' GYD',
            ' HNL	',
            ' HKD',
            ' HUF',
            ' ISK',
            ' INR',
            ' IDR',
            ' IRR',
            ' IMP		',
            ' ILS',
            ' JMD',
            'JPY',
            'KZT',
            ' KPW',
            ' KRW',
            ' KGS',
            ' LAK',
            ' LBP',
            ' LRD',
            ' MKD',
            ' MYR',
            ' MUR	',
            ' MXN',
            ' MNT',
            'MZN',
            ' NAD',
            ' NPR',
            ' ANG',
            ' NZD	',
            ' NIO	',
            ' NGN',
            ' NOK',
            ' OMR	',
            ' PKR	',
            ' PAB',
            ' PYG',
            'PEN',
            'PHP',
            ' PLN',
            ' QAR',
            ' RON',
            ' RUB',
            ' SHP',
            ' SAR',
            ' RSD',
            ' SCR	',
            ' SGD	',
            ' SBD',
            ' SOS',
            'ZAR',
            ' LKR',
            ' SEK	',
            ' CHF',
            ' SRD',
            ' SYP',
            ' TWD',
            ' THB',
            ' TTD',
            ' TRY ',
            ' TVD',
            ' UAH',
            'GBP	',
            ' UYU',
            ' UZS	',
            ' VEF ',
            ' VND',
            ' YER',
            'ZWD'
        ]

        # Image Label
        self.open_image=Image.open(r"C:\Users\Dell\Desktop\image_tk\currency.png")
        self.zoom = 0.5
        self.pixels_x, self.pixels_y = tuple([int(self.zoom * x) for x in self.open_image.size])
        self.image=ImageTk.PhotoImage(self.open_image.resize((self.pixels_x, self.pixels_y)))
        self.image_label=Label(self.root,image=self.image)
        self.image_label.place(x=190,y=35)

        # Labels
        self.title_label=Label(self.root,text="USD Currency Converter Using Python", font=("verdana",10,"bold"))
        self.title_label.place(x=150,y=15)

        self.amount_label=Label(self.root,text="Amount",font=("roboto",10,"bold"))
        self.amount_label.place(x=20,y=15)

        # Entries
        self.amount_entry=Entry(self.root,width=20,borderwidth=1,
                                font=("roboto",10,"bold"),textvariable=self.amount_var)
        self.amount_entry.place(x=20,y=40)

        self.result_entry=Entry(self.root,width=20,borderwidth=1,
                                font=("roboto",10,"bold"),textvariable=self.result_var)
        self.result_entry.place(x=20,y=80)

        # Combo Boxes
        self.currency_combobox=Combobox(self.root,state="readonly",
                                        values=self.currency_values,width = 20
                                        ,font=("verdana",10,"bold"),textvariable=self.currency_var)
        self.currency_combobox.place(x=300,y=80)

        self.usd_combobox=Combobox(self.root,state="readonly",values=("USD",),
                                   font=("verdana",10,"bold"),width = 20,textvariable=self.usd_var)
        self.usd_combobox.place(x=300,y=40)
        self.usd_combobox.current(0)


        # Buttons
        self.search_button=Button(self.root,text="Search",borderwidth=2,bg="red"
                                  ,fg="white",font=("verdana",10,"bold"),command=self.search_thread)
        self.search_button.place(x=20,y=120)

        self.clear_button=Button(self.root,text="Clear",borderwidth=2,bg="blue"
                                  ,fg="white",font=("verdana",10,"bold"),command=self.clear)
        self.clear_button.place(x=20,y=170)

        # Text
        self.info_text=Text(self.root,height=7,width=52,font=("verdana",10,"bold"))
        self.info_text.place(x=100,y=120)

        self.root.mainloop()

    # Search Method
    def search(self):
        try:
            self.currency = self.usd_var.get().strip() + self.currency_var.get().strip()
            if self.amount_var.get() == 0 or self.currency_var.get() =="":
                messagebox.showerror("Currency Converter", "Please Fill the Amount or currency")
            else:
                self.req = requests.get("http://api.currencylayer.com/live?access_key=4273d2c37f738367f08780b934ce7dda&format=1").json()
                self.result_var.set(self.amount_var.get()*self.req["quotes"][self.currency])
                self.info_text.insert(END,f"{self.amount_var.get()} United State Dollar Equals {self.amount_var.get()*self.req['quotes'][self.currency]} {self.currency_var.get()} \n\n Last Time Update --- \t {datetime.now()}")
        except Exception:
            messagebox.showerror("Currency Converter", "Please Fill the Amount or currency")

    # Thread Method
    def search_thread(self):
        self.thread=threading.Thread(target=self.search)
        self.thread.start()


    # Clear Method
    def clear(self):
        self.amount_var.set("")
        self.result_var.set("")
        self.info_text.delete(1.0,END)

if __name__ == "__main__":
    CurrencyConverter()
