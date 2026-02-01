import os
print("Current working directory:", os.getcwd())
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open ("tasks.txt","w") as file:
        for task in tasks:
            file.write(f"{task}\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    print("To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks):
    new_task = input("Enter the new task: ")
    tasks.append(new_task)
    print("Task added successfully.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks: 
        return
    try:
        num = int(input("Enter the task number to delete:"))
        removed_task = tasks.pop(num - 1)
        print(f"Removed task: {removed_task}")
    except (ValueError, IndexError):
            print("Invalid task number.")

tasks = load_tasks()

while True:
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks(tasks)
    elif choice == '2':
        add_task(tasks)
        save_tasks(tasks)
    elif choice == '3':
        delete_task(tasks)
        save_tasks(tasks)
    elif choice == '4':
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        
