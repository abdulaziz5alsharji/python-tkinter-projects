from tkinter import *


class TaskManager:
    def __init__(self):
        # Window Design
        self.root = Tk()
        self.root.geometry("300x360")
        self.root.iconbitmap("task-icon.ico")
        self.root.configure(bg="#9DBEBB")
        self.root.title("Task Manager")
        self.root.resizable(0, 0)
        # VARS
        self.tasks = []
        self.task_var = StringVar()
        # Main Frame
        self.main_frame = Frame(self.root, width=300, height=280, bd=3)
        self.main_frame.pack(pady=10)
        # List Box
        self.task_list_box = Listbox(self.main_frame, font=('arial', 12), width=28, height=12)
        self.task_list_box.pack(fill="both", padx=2, side="left")

        self.eachTasks()
        # scroll bar
        self.task_scroll_bar = Scrollbar(self.main_frame)
        self.task_scroll_bar.pack(side="right", fill="both")
        self.task_list_box.config(yscrollcommand=self.task_scroll_bar.set)
        self.task_scroll_bar.config(command=self.task_list_box.yview)
        # Add Entry
        self.add_entry = Entry(self.root, width=20, font=('times', 14), textvariable=self.task_var)
        self.add_entry.pack(pady=10)
        # Button Frame
        self.button_frame = Frame(self.root, width=280, height=5)
        self.button_frame.pack(pady=10)
        # Add Button
        self.add_button = Button(self.button_frame, text="Add Task", bg='light green', command=self.addTask)
        self.add_button.grid(row=0, column=0)
        # Delete Button
        self.delete_button = Button(self.button_frame, text="Delete Task", bg='#e20049', command=self.deleteTask)
        self.delete_button.grid(row=0, column=1)
        self.root.mainloop()

    def addTask(self):
        task = self.task_var.get()
        if task != "":
            with open("taskFile.txt", "a") as fileTask:
                fileTask.write(f"{task}\n")
            self.task_list_box.insert(END, task)
            self.tasks.append(task)
            self.task_var.set("")

    def deleteTask(self):
        task = str(self.task_list_box.get(ANCHOR))
        if task in self.tasks:
            self.tasks.remove(task)
            with open("taskFile.txt", "w") as file:
                for item in self.tasks:
                    file.write(f"{item}\n")
            self.task_list_box.delete(ANCHOR)

    def eachTasks(self):
        with open("taskFile.txt", "r") as file:
            for task in file.read().split():
                self.tasks.append(task)
                self.task_list_box.insert(END, task)


if __name__ == '__main__':
    TaskManager()
