import sys

try:
    from tkinter import *
    import threading, time
    from datetime import datetime
    from PIL import ImageTk, Image
    from tkinter.filedialog import askdirectory
    from tkinter import messagebox
    from pytube import YouTube
    from pytube import Playlist
    from tkinter.ttk import Progressbar
    from tkinter.scrolledtext import ScrolledText
except ModuleNotFoundError as e:
    print(e)
    input("Press any key to exit ..")
    sys.exit()


class YoutubeDownloader:

    def __init__(self):
        # Widow design

        self.root = Tk()
        self.root.title("Youtube Downloader")
        self.root.geometry("500x270")
        self.root.resizable(0, 0)
        self.root.iconbitmap("youtube-icon.ico")
        self.root.configure(bg="white")

        # Vars

        self.playlist_url_var = StringVar()
        self.playlist_path_var = StringVar()
        self.video_path_var = StringVar()
        self.video_url_var = StringVar()

        # Labels

        self.title_label = Label(self.root, text="Youtube Downloader", font=("verdana", 15, "bold")
                                 , bg="white", fg="red")
        self.title_label.place(x=130, y=5)

        self.date_label = Label(self.root, text=datetime.now(), bg="white", font=("verdana", 10, "bold"))
        self.date_label.place(x=138, y=45)

        # Label Design

        self.line_design_label_one = Label(self.root, bg="red", width=19)
        self.line_design_label_one.place(x=0, y=45)

        self.line_design_label_two = Label(self.root, bg="red", width=19)
        self.line_design_label_two.place(x=360, y=45)

        self.line_design_label_three = Label(self.root, bg="red", width=3, height=6)
        self.line_design_label_three.place(x=242, y=90)

        # Image Label

        self.image = ImageTk.PhotoImage(Image.open("youtube.png"))
        self.image_label = Label(self.root, image=self.image, bg="white")
        self.image_label.place(x=220, y=70)

        # Buttons

        self.clear_button = Button(self.root, text="Clear", bg="white", fg="red", padx=10
                                   , relief=RAISED, font=("verdana", 10, "bold"), borderwidth=3
                                   , command=self.clear)
        self.clear_button.place(x=220, y=195)

        self.quit_button = Button(self.root, text="Quit", bg="red", fg="white", padx=15
                                  , relief=RAISED, font=("verdana", 10, "bold"), borderwidth=3
                                  , command=self.quit)
        self.quit_button.place(x=220, y=230)

        # Label Frames

        # Label Frame Video

        self.video_label_frame = LabelFrame(self.root, text="Download Video", width=180, height=180,
                                            font=('verdana', 10, 'bold'), bg="white", fg="red", borderwidth=5
                                            , relief=SUNKEN, highlightcolor="red", highlightbackground="red")
        self.video_label_frame.place(x=10, y=80)

        # Label Frame PlayList

        self.playlist_label_frame = LabelFrame(self.root, text="Download Playlist", width=180, height=180,
                                               font=('verdana', 10, 'bold')
                                               , bg="white", fg="red",
                                               borderwidth=5, relief=SUNKEN, highlightcolor="red"
                                               , highlightbackground="red")
        self.playlist_label_frame.place(x=310, y=80)

        # Video Downloader Form

        self.video_url_label = Label(self.video_label_frame, text="Paste url Here ...",
                                     font=('verdana', 10, 'bold'), bg="white")
        self.video_url_label.place(x=20, y=2)

        self.video_path_label = Label(self.video_label_frame, text="Select Path",
                                      font=('verdana', 10, 'bold'), bg="white")
        self.video_path_label.place(x=10, y=60)

        self.video_url_entry = Entry(self.video_label_frame, width=24, relief=SUNKEN,
                                     borderwidth=2, bg="red", fg="white",
                                     textvariable=self.video_url_var)
        self.video_url_entry.place(x=10, y=30)

        self.video_path_entry = Entry(self.video_label_frame, width=15, relief=SUNKEN
                                      , borderwidth=2, bg="red", fg="white", textvariable=self.video_path_var)
        self.video_path_entry.place(x=10, y=90)

        self.video_path_button = Button(self.video_label_frame, text="Browser",
                                        font=('verdana', 8, 'bold')
                                        , relief=RAISED, bg="white", command=self.select_video_path)
        self.video_path_button.place(x=105, y=88)

        self.download_button = Button(self.video_label_frame, text="Download", font=('verdana', 9, 'bold')
                                      , relief=RAISED, bg="white", borderwidth=4,
                                      command=self.video_download_thread)
        self.download_button.place(x=40, y=125)

        # PlayList Downloader Form

        self.playlist_url_label = Label(self.playlist_label_frame, text="Paste url Here ...",
                                        font=('verdana', 10, 'bold'), bg="white")
        self.playlist_url_label.place(x=20, y=2)

        self.playlist_path_label = Label(self.playlist_label_frame, text="Select Path",
                                         font=('verdana', 10, 'bold'), bg="white")
        self.playlist_path_label.place(x=10, y=60)

        self.playlist_url_entry = Entry(self.playlist_label_frame, width=24, relief=SUNKEN,
                                        borderwidth=2, bg="red", fg="white"
                                        , textvariable=self.playlist_url_var)
        self.playlist_url_entry.place(x=10, y=30)

        self.playlist_path_entry = Entry(self.playlist_label_frame, width=15, relief=SUNKEN
                                         , borderwidth=2, bg="red", fg="white",
                                         textvariable=self.playlist_path_var)
        self.playlist_path_entry.place(x=10, y=90)

        self.playlist_path_button = Button(self.playlist_label_frame, text="Browser",
                                           font=('verdana', 8, 'bold')
                                           , relief=RAISED, bg="white", command=self.select_playlist_path)
        self.playlist_path_button.place(x=105, y=88)

        self.playlist_download_button = Button(self.playlist_label_frame, text="Download", font=('verdana', 9, 'bold')
                                               , relief=RAISED, bg="white", borderwidth=4,
                                               command=self.playlist_download_thread)
        self.playlist_download_button.place(x=40, y=125)

        # Window Loop
        self.root.mainloop()

    # Clear Method
    def clear(self):
        self.video_path_var.set("")
        self.video_url_var.set("")
        self.playlist_path_var.set("")
        self.playlist_url_var.set("")

    # Quit Method
    def quit(self):

        self.check = messagebox.askyesno("Quit", "Do you want to exit the program")
        if self.check:
            self.root.destroy()
        else:
            pass

    def select_video_path(self):

        self.video_path = askdirectory()
        self.video_path_var.set(self.video_path)

    def select_playlist_path(self):
        self.playlist_path = askdirectory()
        self.playlist_path_var.set(self.playlist_path)

    def video_download(self):
        if self.video_path_var.get() == "" or self.video_url_var.get() == "":
            messagebox.showerror("Error", "Please Paste Video URL or PATH")
        elif "https://" not in self.video_url_var.get():
            messagebox.showerror("Error", "Wrong Video Url")
        else:
            try:
                # Video Downloading
                self.video_downloading = YouTube(self.video_url_var.get())
                self.video_streams = self.video_downloading.streams.filter(only_video=True).first()
                print("download started", self.video_downloading.title)

                print("download completed", self.video_downloading.title)

                self.video_streams.download(output_path=self.video_path_var.get())
                # Window Design

                self.video_window = Tk()
                self.video_window.geometry("300x150")
                self.video_window.resizable(0, 0)
                self.video_window.title("Video Downloading")
                self.video_window.iconbitmap("youtube-icon.ico")
                self.video_window.configure(bg="white")

                # Start Download Label
                self.start_video_download_label = Label(self.video_window, text="Video downloading .....",
                                                        fg="red", font=('verdana', 10, 'bold'), bg="white")
                self.start_video_download_label.place(x=40, y=10)

                # Video Progress
                self.video_progress = Progressbar(self.video_window, orient=HORIZONTAL, length=250
                                                  , mode="determinate")
                self.video_progress.place(x=20, y=40)
                self.video_progress['value'] = 20
                self.video_window.update_idletasks()
                self.video_progress['value'] = 40
                self.video_window.update_idletasks()
                self.video_progress['value'] = 60
                self.video_window.update_idletasks()
                self.video_progress['value'] = 80
                self.video_window.update_idletasks()
                self.video_progress['value'] = 100
                self.video_window.update_idletasks()

                # Video Details Text
                self.video_details_text = ScrolledText(self.video_window,
                                                       width=30, height=3, font=('verdana', 8, 'bold'))
                self.video_details_text.place(x=20, y=70)

                self.video_details_text.insert(END, f"{self.video_downloading.title}\n{self.video_path_var.get()}")

                # Download Status Label
                self.download_status_label = Label(self.video_window, text="Video downloaded successfully ....."
                                                   , fg="red", font=('verdana', 10, 'bold'), bg="white")
                self.download_status_label.place(x=10, y=120)

                self.video_window.mainloop()

            except Exception:
                messagebox.showerror("error", "Unable to Download Video | Something went wrong !!")

    def video_download_thread(self):
        thread_video = threading.Thread(target=self.video_download)
        thread_video.start()

    def playlist_download(self):
        if self.playlist_path_var.get() == "" or self.playlist_url_var.get() == "":
            messagebox.showerror("Error", "Please Paste Playlist URL or PATH")
        elif "https://" not in self.playlist_url_var.get():
            messagebox.showerror("Error", "Wrong Playlist Url")
        else:
            try:
                # Video Downloading
                self.playlist_downloading = Playlist(self.playlist_url_var.get())

                for video in self.playlist_downloading:
                    video.streams.get_highest_resolution().download(output_path=self.playlist_path_var.get())

                # Window Design

                self.playlist_window = Tk()
                self.playlist_window.geometry("300x150")
                self.playlist_window.resizable(0, 0)
                self.playlist_window.title("Playlist Downloading")
                self.playlist_window.iconbitmap(r"C:\Users\Dell\Desktop\icon\youtube-icon.ico")
                self.playlist_window.configure(bg="white")

                # Start Download Label
                self.start_playlist_download_label = Label(self.playlist_window, text="playlist downloading .....",
                                                           fg="red", font=('verdana', 10, 'bold'), bg="white")
                self.start_playlist_download_label.place(x=40, y=10)

                # Video Progress
                self.playlist_progress = Progressbar(self.playlist_window, orient=HORIZONTAL, length=250
                                                     , mode="determinate")
                self.playlist_progress.place(x=20, y=40)
                self.playlist_progress['value'] = 20
                self.playlist_window.update_idletasks()
                self.playlist_progress['value'] = 40
                self.playlist_window.update_idletasks()
                self.playlist_progress['value'] = 60
                self.playlist_window.update_idletasks()
                self.playlist_progress['value'] = 80
                self.playlist_window.update_idletasks()
                self.playlist_progress['value'] = 100
                self.playlist_window.update_idletasks()

                # Video Details Text
                self.playlist_details_text = ScrolledText(self.playlist_window,
                                                          width=30, height=3, font=('verdana', 8, 'bold'))
                self.playlist_details_text.place(x=20, y=70)

                # self.playlist_details_text.insert(END, f"{self.video_downloading.title}\n{self.video_path_var.get()}")

                # Download Status Label
                self.download_status_label_p = Label(self.playlist_window, text="playlist downloaded successfully ....."
                                                     , fg="red", font=('verdana', 10, 'bold'), bg="white")
                self.download_status_label_p.place(x=10, y=120)

                self.playlist_window.mainloop()

            except Exception:
                messagebox.showerror("error", "Unable to Download Playlist | Something went wrong !!")

    def playlist_download_thread(self):
        thread_playlist = threading.Thread(target=self.playlist_download)
        thread_playlist.start()


if __name__ == "__main__":
    YoutubeDownloader()
