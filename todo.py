# todo.py

FILENAME = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()

# Remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            removed = tasks.pop(index - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number!")

# Main menu
def main():
    tasks = load_tasks()
    
    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()
