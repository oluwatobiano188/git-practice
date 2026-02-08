"""
Simple Todo List Application
Practice Git with this project!
"""

tasks = []

def show_menu():
    print("\n=== TODO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to delete: "))
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("\nChoose option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
