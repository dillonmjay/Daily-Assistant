import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import time
import datetime

class DailyAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Assistant")

        self.tasks = []

        # Main Frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=20, padx=20)

        # Buttons
        self.add_task_btn = tk.Button(self.main_frame, text="Add Task", command=self.add_task)
        self.add_task_btn.grid(row=0, column=0, padx=10, pady=10)

        self.view_tasks_btn = tk.Button(self.main_frame, text="View Tasks", command=self.view_tasks)
        self.view_tasks_btn.grid(row=0, column=1, padx=10, pady=10)

        self.set_reminder_btn = tk.Button(self.main_frame, text="Set Reminder", command=self.set_reminder)
        self.set_reminder_btn.grid(row=1, column=0, padx=10, pady=10)

        self.calculator_btn = tk.Button(self.main_frame, text="Quick Calculator", command=self.quick_calculator)
        self.calculator_btn.grid(row=1, column=1, padx=10, pady=10)

        self.date_time_btn = tk.Button(self.main_frame, text="Date & Time", command=self.check_date_time)
        self.date_time_btn.grid(row=2, column=0, padx=10, pady=10)

        self.exit_btn = tk.Button(self.main_frame, text="Exit", command=root.quit)
        self.exit_btn.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a new task:")
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Success", "Task added successfully!")


    def view_tasks(self):
        if self.tasks:
            tasks_str = "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(self.tasks))
            messagebox.showinfo("Your Tasks", tasks_str)
        else:
            messagebox.showinfo("No Tasks", "You have no tasks. Add some!")

    def set_reminder(self):
        reminder = tk.simpledialog.askstring("Set Reminder", "Enter your reminder:")
        try:
            delay = int(tk.simpledialog.askstring("Set Reminder", "Enter time in seconds:"))
            messagebox.showinfo("Reminder Set", f"Reminder set! You will be reminded in {delay} seconds.")
            self.root.after(delay * 1000, lambda: messagebox.showinfo("Reminder", reminder))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for seconds.")

    def quick_calculator(self):
        expression = tk.simpledialog.askstring("Quick Calculator", "Enter your expression (e.g., 5 + 3):")
        try:
            result = eval(expression)
            messagebox.showinfo("Result", f"The result is: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {e}")

    def check_date_time(self):
        now = datetime.datetime.now()
        messagebox.showinfo("Date & Time", now.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyAssistant(root)
    root.mainloop()
