import time
import datetime
import math

def display_menu():
    print("\n=== Daily Assistant ===")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Set a Reminder")
    print("4. Quick Calculator")
    print("5. Check Date and Time")
    print("6. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks available. Add some!")

