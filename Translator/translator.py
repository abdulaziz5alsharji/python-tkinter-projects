try:
    from tkinter import *
    from PIL import ImageTk, Image
    from googletrans import Translator
    from tkinter import messagebox
    from tkinter.ttk import Combobox
    from threading import Thread
except ModuleNotFoundError as error:
    import sys
    print(error)
    input("Enter To Exit >>")
    sys.exit()

class Translate:
    def __init__(self):
        # Window Design
        self.root=Tk()
        self.root.geometry("530x330")
        self.root.title("Languages Translator")
        self.root.resizable(0,0)
        self.root.iconbitmap(r"translator.ico")

        # Combo Values
        self.languages=[
            'Afrikaans',
            'Albanian',
            'Arabic',
            'Armenian',
            ' Azerbaijani',
            'Basque',
            'Belarusian',
            'Bengali',
            'Bosnian',
            'Bulgarian',
            ' Catalan',
            'Cebuano',
            'Chichewa',
            'Chinese',
            'Corsican',
            'Croatian',
            ' Czech',
            'Danish',
            'Dutch',
            'English',
            'Esperanto',
            'Estonian',
            'Filipino',
            'Finnish',
            'French',
            'Frisian',
            'Galician',
            'Georgian',
            'German',
            'Greek',
            'Gujarati',
            'Haitian Creole',
            'Hausa',
            'Hawaiian',
            'Hebrew',
            'Hindi',
            'Hmong',
            'Hungarian',
            'Icelandic',
            'Igbo',
            'Indonesian',
            'Irish',
            'Italian',
            'Japanese',
            'Javanese',
            'Kannada',
            'Kazakh',
            'Khmer',
            'Kinyarwanda',
            'Korean',
            'Kurdish',
            'Kyrgyz',
            'Lao',
            'Latin',
            'Latvian',
            'Lithuanian',
            'Luxembourgish',
            'Macedonian',
            'Malagasy',
            'Malay',
            'Malayalam',
            'Maltese',
            'Maori',
            'Marathi',
            'Mongolian',
            'Myanmar',
            'Nepali',
            'Norwegian'
            'Odia',
            'Pashto',
            'Persian',
            'Polish',
            'Portuguese',
            'Punjabi',
            'Romanian',
            'Russian',
            'Samoan',
            'Scots Gaelic',
            'Serbian',
            'Sesotho',
            'Shona',
            'Sindhi',
            'Sinhala',
            'Slovak',
            'Slovenian',
            'Somali',
            'Spanish',
            'Sundanese',
            'Swahili',
            'Swedish',
            'Tajik',
            'Tamil',
            'Tatar',
            'Telugu',
            'Thai',
            'Turkish',
            'Turkmen',
            'Ukrainian',
            'Urdu',
            'Uyghur',
            'Uzbek',
            'Vietnamese',
            'Welsh',
            'Xhosa'
            'Yiddish',
            'Yoruba',
            'Zulu']

        # Vars
        self.lang_var=StringVar()
        # Image Label
        self.image=ImageTk.PhotoImage(Image.open(r"translator.png"))
        self.label_image=Label(self.root,image=self.image)
        self.label_image.place(x=230,y=3)

        # Combo Box 1
        self.cobo_box_1=Combobox(self.root,values=("Auto Detect",),width = 20,
                                 state='readonly',font=('verdana',10,'bold'))
        self.cobo_box_1.place(x=30,y=70)
        self.cobo_box_1.current(0)

        # Combo Box 2
        self.languages_combo_box=Combobox(self.root,values=self.languages,width = 20,
                                          state="readonly",font=("verdana",10,"bold")
                                          ,textvariable=self.lang_var)
        self.languages_combo_box.place(x=290,y=70)
        self.languages_combo_box.current(0)

        # Text 1
        self.first_text=Text(self.root,width=30,height=10,borderwidth=5,relief=RIDGE)
        self.first_text.place(x=10,y=100)

        # Text 2
        self.second_text=Text(self.root,width=30,height=10,borderwidth=5,relief=RIDGE)
        self.second_text.place(x=260,y=100)

        # Button 1
        self.clear_button=Button(self.root,text="Clear",relief=RIDGE,borderwidth=3
                                 ,font=("verdana",10,"bold"),cursor="hand2",command=self.clear)
        self.clear_button.place(x=280,y=280)

        # Button 2
        self.translate_button=Button(self.root,text="Translate",relief=RIDGE,borderwidth=3
                                     ,font=("verdana",10,"bold"),cursor="hand2",command=self.translate_thread)
        self.translate_button.place(x=150,y=280)
        self.root.mainloop()

    # Clear Function
    def clear(self):
        self.first_text.delete(1.0,END)
        self.second_text.delete(1.0,END)

    # Translate Function
    def translate(self):
        try:
            self.language=self.lang_var.get()
            self.text=self.first_text.get(1.0,"end-1c")
            if self.text == "":
                messagebox.showerror("Language Translator","please fill the box")
            else:
                self.second_text.delete(1.0, END)
                self.translator = Translator()
                self.second_text.insert(END,self.translator.translate(self.text, dest=self.language).text)
        except Exception as e:
            messagebox.showerror("Language Translator", e)

    # Thread Function
    def translate_thread(self):
        self.thread=Thread(target=self.translate)
        self.thread.start()


if __name__ =="__main__":
    Translate()
