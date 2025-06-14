# To Do list
from sys import orig_argv
from turtledemo.penrose import start


def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a willing task")
    print("2. View tasks")
    print("3. Remove a unnecessary task")
    print("3. Exit")

def main():
    todo_list = []

    while True:
        show_menu()
        choice = input("Choose an option (1-4) ")

        if choice == "1":
            task = input("Enter the task:")
            todo_list.append(task)
            print(f"Task '{task}' added.")

        elif choice == "2":
            if not todo_list:
                print("Your To Do list is empty.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(todo_list, start= 1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not todo_list:
                print("Your to-do list is empty, nothing to remove.")
            else:
                print("\nTasks:")
                for i, task in enumerate(todo_list, start=1):
                    print(f"{i}.{task}")
                task_num = input("Enter the number of the task to remove: ")
                if task_num.isdigit() and 1 <= int(task_num) <= len(todo_list):
                    removed = todo_list.pop(int(task_num) - 1)
                    print(f"Removed task: {removed}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()