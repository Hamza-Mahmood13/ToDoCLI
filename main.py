import json
import os

FILENAME = "tasks.json"

def load_tasks():
    #This is to load the json file, if it exists
    try:
        with open(FILENAME, 'r') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    #This will save the json file after changes that have been made
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def check_file():
    #Checks json file exists
    if not os.path.exists(FILENAME):
        save_tasks([])

def print_tasks(tasks):
    #Prints out tasks that are in the json file, in numbered order, and in clean text format
    print("Your tasks: ")
    if not tasks:
        print("No tasks found.")
        return False
    
    for i, j in enumerate(tasks, start = 1):
        desc = j.get("task", "<no description>")
        done = j.get("done", False)
        status = "YES" if done else "X"
        print(f"{i}. {desc} [{status}]")
    return True

def ask_number(prompt):
    #Validation of any questions asked by the program to make sure they are suitable
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        return None

def main():

    check_file()

    while True:
        print("To do list")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark tasks as done")
        print("4. Delete tasks")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            tasks = load_tasks()
    
            new_task = input("Enter new task: ").strip()
            if not new_task:
                print("Task cannot be empty.")
                continue

            tasks.append({"task": new_task, "done": False})
            save_tasks(tasks)
            print("Task added")

        elif choice == "2":
            tasks = load_tasks()
            print_tasks(tasks)
            
        elif choice == "3":
            tasks = load_tasks()
            if not print_tasks(tasks):
                continue

            task_num = ask_number("Which task would you like to update? ")
            if task_num is None:
                print("Please enter a valid number.")
                continue

            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = not tasks[task_num-1]["done"]
                save_tasks(tasks)
                print("Task updated")
            else:
                print("Invalid task number.")
                continue

        elif choice == "4":
            tasks = load_tasks()
            if not print_tasks(tasks):
                continue

            remove_task  = ask_number("Which task would you like to delete? ")
            if remove_task is None:
                print("Please enter a valid number.")
                continue

            if 1 <= remove_task <= len(tasks):
                removed = tasks.pop(remove_task - 1)
                save_tasks(tasks)
                print(f"Deleted: {removed.get('task', '<no description')}")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Try again")
        
main()
