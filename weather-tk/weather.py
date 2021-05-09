try:
    from tkinter import *
    import tkinter as tk
    from datetime import datetime
    from PIL import ImageTk, Image
    import requests
    from tkinter import messagebox
    from threading import Thread
except ModuleNotFoundError as e:
    import sys

    print(e)
    input("Enter to exit >>")
    sys.exit()


# Start Weather Class
class Weather:
    def __init__(self):
        # Window Design
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Weather Application")
        self.root.iconbitmap(r"weather-icon.ico")
        self.root.resizable(0, 0)
        self.font = ('verdana', 10, 'bold')
        # Labels
        # Header
        self.header_label = Label(self.root, bg="#00274c", width=100, height=2)
        self.header_label.pack()
        # Date Label
        self.date_label = Label(self.root, text=datetime.now().date(), bg="#00274c", fg="white", font=self.font)
        self.date_label.place(x=400, y=5)
        # Title Label
        self.title_label = Label(self.root, text="Weather Report", bg="#00274c", fg="white", font=self.font)
        self.title_label.place(x=180, y=5)
        # Location Label
        self.location_label = Label(self.root, text="NA-/", bg="#00274c", fg="white", font=self.font)
        self.location_label.place(x=10, y=5)
        # Image(1)
        self.img = ImageTk.PhotoImage(Image.open(r"icon.png"))
        self.image_label = Label(self.root, image=self.img)
        self.image_label.place(x=20, y=40)
        # Caption Label
        self.caption_label = Label(self.root, text="City or Country Name: ^_^", fg="#00274c", font=self.font)
        self.caption_label.place(x=140, y=45)
        # City Text
        self.city_text = Text(self.root, width=25, height=2)
        self.city_text.place(x=140, y=70)
        # Search Button
        self.search_button = Button(self.root, text="Search", fg="white", bg="#00274c", relief="raised", font=self.font,
                                    borderwidth=3,
                                    command=self.weather_report_thread)
        self.search_button.place(x=350, y=73)
        # Design Label
        self.design1 = Label(self.root, bg="#00274c", width=20, height=0)
        self.design1.place(x=0, y=150)
        self.design2 = Label(self.root, bg="#00274c", width=20, height=0)
        self.design2.place(x=360, y=150)
        # Report Label
        self.report_label = Label(self.root, text="Weather Report", bg="#00274c", fg="white", font=self.font, padx=10)
        self.report_label.place(x=180, y=150)

        # Icon Label (1)
        self.icon_1 = ImageTk.PhotoImage(Image.open(r"icon2.png"))
        self.ico_label_1 = Label(self.root, image=self.icon_1)
        self.ico_label_1.place(x=90, y=180)
        self.weather_label = Label(self.root, text="NA/-", fg="#00274c", font=self.font)
        self.weather_label.place(x=90, y=230)
        # Icon Label (2)
        self.icon_2 = ImageTk.PhotoImage(Image.open(r"icon3.png"))
        self.ico_label_2 = Label(self.root, image=self.icon_2)
        self.ico_label_2.place(x=200, y=180)
        self.temperature_label = Label(self.root, text="NA/-", fg="#00274c", font=self.font)
        self.temperature_label.place(x=200, y=230)
        # Icon Label (3)
        self.icon_3 = ImageTk.PhotoImage(Image.open(r"icon4.png"))
        self.ico_label_3 = Label(self.root, image=self.icon_3)
        self.ico_label_3.place(x=310, y=180)
        self.humidity_label = Label(self.root, text="NA/-", fg="#00274c", font=self.font)
        self.humidity_label.place(x=310, y=230)
        # Icon Label (4)
        self.icon_4 = ImageTk.PhotoImage(Image.open(r"icon5.png"))
        self.ico_label_4 = Label(self.root, image=self.icon_4)
        self.ico_label_4.place(x=380, y=180)
        self.pressure_label = Label(self.root, text="NA/-", fg="#00274c", font=self.font)
        self.pressure_label.place(x=380, y=230)

        self.root.mainloop()

    # Button Function
    def weather_report(self):
        try:
            city_name = self.city_text.get(1.0, END)
            api_key = "6c8fe7679edd72690ade111f97bf3ecc"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
            req = requests.get(url).json()
            cloud = req["weather"][0]["description"]
            pressure = req["main"]["pressure"]
            country = req["sys"]["country"]
            humidity = req["main"]["humidity"]
            city = req["name"]
            temp_c = req["main"]["temp_max"] - 273.15
            temp_f = temp_c * 9 / 5 + 32
            if req["cod"] == "404":
                messagebox.showerror("ERROR", "City Not Found !!")
            else:
                self.location_label.configure(text=f"{city},{country}")
                self.weather_label.configure(text=cloud)
                self.temperature_label.configure(text=f"{temp_c}°C \n {temp_f}°F")
                self.humidity_label.configure(text=humidity)
                self.pressure_label.configure(text=pressure)
        except Exception as error:
            print(error)
            messagebox.showerror("Exception", "City Only..")

    def weather_report_thread(self):
        thread = Thread(target=self.weather_report)
        thread.start()


if __name__ == "__main__":
    Weather()
