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

def set_reminder():
    reminder = input("Enter your reminder: ")
    delay = int(input("Enter time in seconds after which you want to be reminded: "))
    print(f"Reminder set! You will be reminded in {delay} seconds.")
    time.sleep(delay)
    print(f"\nReminder: {reminder}")

def quick_calculator():
    print("\nSimple Calculator")
    print("Enter your expression (e.g., 5 + 3 or 12 / 4):")
    try:
        expression = input(">> ")
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error in calculation: {e}")

def check_date_time():
    now = datetime.datetime.now()
    print("\nCurrent Date and Time:")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            set_reminder()
        elif choice == '4':
            quick_calculator()
        elif choice == '5':
            check_date_time()
        elif choice == '6':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
