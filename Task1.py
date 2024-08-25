import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            old_task = self.tasks[task_number]
            self.tasks[task_number] = new_task
            print(f"Updated task {task_number}: {old_task} -> {new_task}")
        else:
            print("Invalid task number")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Deleted task {task_number}: {removed_task}")
        else:
            print("Invalid task number")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"{idx}: {task}")

def print_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. Update task")
    print("3. Delete task")
    print("4. Display tasks")
    print("5. Exit")

def main():
    todo_list = ToDoList()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
        elif choice == "3":
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()