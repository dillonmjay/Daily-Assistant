import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import time
import datetime

class DailyAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Assistant")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e1e")

        self.tasks = []

        # Modern Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=("Helvetica", 14))
        style.configure("TButton", background="#2b2b2b", foreground="#ffffff", font=("Helvetica", 12), padding=5, borderwidth=1)
        style.map("TButton", background=[("active", "#333333")], relief=[("active", "groove")])

        # Header Frame
        header_frame = ttk.Frame(root)
        header_frame.pack(fill="x", pady=10)

        title_label = ttk.Label(header_frame, text="Daily Assistant", font=("Helvetica", 24, "bold"), anchor="center")
        title_label.pack()

        subtitle_label = ttk.Label(header_frame, text="Your Personal Day-to-Day Helper", font=("Helvetica", 12), anchor="center")
        subtitle_label.pack()

        # Main Frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(expand=True)

        # Center Buttons in a Grid
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

        # Buttons with rounded corners
        self.add_task_btn = ttk.Button(self.main_frame, text="📝 Add Task", command=self.add_task, style="TButton")
        self.add_task_btn.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.add_hover_effect(self.add_task_btn)

        self.view_tasks_btn = ttk.Button(self.main_frame, text="📋 View Tasks", command=self.view_tasks, style="TButton")
        self.view_tasks_btn.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.add_hover_effect(self.view_tasks_btn)

        self.set_reminder_btn = ttk.Button(self.main_frame, text="⏰ Set Reminder", command=self.set_reminder, style="TButton")
        self.set_reminder_btn.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.add_hover_effect(self.set_reminder_btn)

        self.calculator_btn = ttk.Button(self.main_frame, text="➕ Quick Calculator", command=self.quick_calculator, style="TButton")
        self.calculator_btn.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.add_hover_effect(self.calculator_btn)

        self.date_time_btn = ttk.Button(self.main_frame, text="📅 Date & Time", command=self.check_date_time, style="TButton")
        self.date_time_btn.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        self.add_hover_effect(self.date_time_btn)

        self.exit_btn = ttk.Button(self.main_frame, text="❌ Exit", command=root.quit, style="TButton")
        self.exit_btn.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.add_hover_effect(self.exit_btn)

    def add_hover_effect(self, button):
        def on_enter(event):
            button.configure(style="Hover.TButton")
        def on_leave(event):
            button.configure(style="TButton")

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a new task:")
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Success", "Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            tasks_str = "\n".join(f"{idx + 1}. {task}" for idx, task in enumerate(self.tasks))
            task_window = tk.Toplevel(self.root)
            task_window.title("Your Tasks")
            task_window.geometry("400x300")
            task_window.configure(bg="#1e1e1e")

            ttk.Label(task_window, text="Your Tasks", font=("Helvetica", 16, "bold"), background="#1e1e1e", foreground="#ffffff", anchor="center").pack(pady=10)
            ttk.Label(task_window, text=tasks_str, font=("Helvetica", 12), background="#1e1e1e", foreground="#ffffff", anchor="center").pack(pady=10)
        else:
            messagebox.showinfo("No Tasks", "You have no tasks. Add some!")

    def set_reminder(self):
        reminder = simpledialog.askstring("Set Reminder", "Enter your reminder:")
        try:
            delay = int(simpledialog.askstring("Set Reminder", "Enter time in seconds:"))
            reminder_window = tk.Toplevel(self.root)
            reminder_window.title("Reminder Set")
            reminder_window.geometry("400x200")
            reminder_window.configure(bg="#1e1e1e")

            ttk.Label(reminder_window, text=f"Reminder will trigger in {delay} seconds!", font=("Helvetica", 14), background="#1e1e1e", foreground="#ffffff", anchor="center").pack(pady=10)
            self.root.after(delay * 1000, lambda: messagebox.showinfo("Reminder", reminder))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for seconds.")

    def quick_calculator(self):
        calculator_window = tk.Toplevel(self.root)
        calculator_window.title("Quick Calculator")
        calculator_window.geometry("400x200")
        calculator_window.configure(bg="#1e1e1e")

        ttk.Label(calculator_window, text="Quick Calculator", font=("Helvetica", 16, "bold"), background="#1e1e1e", foreground="#ffffff", anchor="center").pack(pady=10)
        expression_entry = ttk.Entry(calculator_window, font=("Helvetica", 12))
        expression_entry.pack(pady=10)

        def calculate():
            expression = expression_entry.get()
            try:
                result = eval(expression)
                messagebox.showinfo("Result", f"The result is: {result}")
            except Exception as e:
                messagebox.showerror("Error", f"Invalid expression: {e}")

        ttk.Button(calculator_window, text="Calculate", command=calculate, style="TButton").pack(pady=10)

    def check_date_time(self):
        now = datetime.datetime.now()
        date_time_window = tk.Toplevel(self.root)
        date_time_window.title("Date & Time")
        date_time_window.geometry("400x200")
        date_time_window.configure(bg="#1e1e1e")

        ttk.Label(date_time_window, text="Current Date & Time", font=("Helvetica", 16, "bold"), background="#1e1e1e", foreground="#ffffff", anchor="center").pack(pady=10)
        ttk.Label(date_time_window, text=now.strftime("%Y-%m-%d %H:%M:%S"), font=("Helvetica", 14), background="#1e1e1e", foreground="#ffffff", anchor="center").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = DailyAssistant(root)
    root.mainloop()
