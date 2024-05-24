import os

class TodoList:
    def __init__(self, filename="todo.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list")
        else:
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + "\n")
        print("Tasks saved")

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = [line.strip() for line in file]
            print("Tasks loaded")

    def clear_tasks(self):
        self.tasks = []
        print("All tasks cleared")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Save tasks")
        print("5. Clear tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number")
        elif choice == '4':
            todo_list.save_tasks()
        elif choice == '5':
            todo_list.clear_tasks()
        elif choice == '6':
            todo_list.save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()