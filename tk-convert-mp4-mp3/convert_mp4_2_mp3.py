import sys

try:
    import threading
    import os
    import moviepy.editor
    from tkinter import *
    from tkinter import messagebox
    from tkinter import filedialog
    from termcolor import colored
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("Press Any Key To Exit ...", color="red"))
    sys.exit()


class ExtractAudioApp:
    def __init__(self):
        # Start Window
        self.root = Tk()
        self.root.title("Extract Audio")
        self.root.geometry("400x200")
        self.root.resizable(0, 0)
        self.root.configure(bg="#993333")
        self.root.iconbitmap("audio-icon.ico")
        self.path = ""
        self.output = ""
        # End Window
        # Title Label
        self.title_label = Label(self.root, text="Extract Audio From Video", bg="#993333", fg="#FFF",
                                 font=("verdana", 12, "bold"))
        self.title_label.pack(fill="x")
        # Path Video Button
        self.path_video_button = Button(self.root, text="Video", bg="#993333", fg="#FFF",
                                        font=("verdana", 12, "bold"), command=self.videoPath)
        self.path_video_button.place(x=120, y=50)
        # Convert
        self.convert_button = Button(self.root, text="Convert", bg="#993333", fg="#FFF",
                                     font=("verdana", 12, "bold"), command=self.convertThread)
        self.convert_button.place(x=200, y=50)
        # Run Button
        self.run_button = Button(self.root, text="Run", bg="#993333", fg="#FFF",
                                 font=("verdana", 12, "bold"), command=self.run)
        self.run_button.place(x=180, y=100)
        # Exit Button
        self.exit_button = Button(self.root, text="Exit", bg="#993333", fg="#FFF",
                                  font=("verdana", 12, "bold"), command=self.exit_)
        self.exit_button.place(x=180, y=140)
        self.root.mainloop()

    def videoPath(self):
        self.path = filedialog.askopenfilename()

    def convert(self):
        if self.path == "":
            messagebox.showerror("error", "Select Path")
            return
        try:
            self.output = self.path.replace("mp4", "mp3")
            video = moviepy.editor.VideoFileClip(self.path)
            audio = video.audio
            audio.write_audiofile(self.output)
            messagebox.showinfo("Done", "Extract Done....")
        except Exception as er:
            messagebox.showerror("error", er)

    def run(self):
        if self.output == "":
            messagebox.showerror("Error", "No Convert")
            return
        os.system(self.output)

    def exit_(self):
        check = messagebox.askyesno("Exit", "Do you want to exit")
        if check:
            self.root.destroy()

    def convertThread(self):
        thread = threading.Thread(target=self.convert)
        thread.start()


if __name__ == '__main__':
    ExtractAudioApp()
