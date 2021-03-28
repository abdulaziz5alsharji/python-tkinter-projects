
try:
    from pyautogui import screenshot
    from tkinter import Button,Label
    from tkinter.filedialog import *
except ModuleNotFoundError as e:
    import sys
    print(e)
    input("Enter to exit..")
    sys.exit()
#here window
root=Tk()
root.geometry("300x200")
root.resizable(0,0)
root.configure(bg="black")
root.title("Take screenshot")
root.iconbitmap(r"C:\Users\Dell\Desktop\icon\screenshot.ico")
#here coding
def screenshot_():
    take_screenshot=screenshot()
    save_path=asksaveasfilename()
    take_screenshot.save(f"{save_path}_screenshot.png")




#Button
bt=Button(root,text="Take ScreenShot",bg="black",fg="white",
          font=("serif",10,"bold"),bd=3
          ,width=20,command=screenshot_)
bt.place(x=70,y=80)
#Label
lb=Label(root,text="ScreenShot",bg="black",fg="white",font=("serif",25,"bold"))
lb.pack()


root.mainloop()
