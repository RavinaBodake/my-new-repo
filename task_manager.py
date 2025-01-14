
import os
import json

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nCompleted: {self.completed}"

    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            print(f"Task {idx}:\n{task}\n")

    def mark_task_completed(self, task_index):
        try:
            task = self.tasks[task_index - 1]
            task.mark_completed()
            print(f"Task '{task.title}' marked as completed.")
        except IndexError:
            print(f"Task {task_index} does not exist!")

    def save_tasks(self):
        try:
            with open(self.filename, "w") as file:
                tasks_data = [vars(task) for task in self.tasks]
                json.dump(tasks_data, file, indent=4)
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    tasks_data = json.load(file)
                    self.tasks = [Task(task['title'], task['description']) for task in tasks_data]
                    for task, data in zip(self.tasks, tasks_data):
                        task.completed = data['completed']
                print("Tasks loaded successfully.")
            except Exception as e:
                print(f"Error loading tasks: {e}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task Completed")
        print("4. Save Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.add_task(title, description)

        elif choice == "2":
            task_manager.display_tasks()

        elif choice == "3":
            task_index = int(input("Enter task number to mark as completed: "))
            task_manager.mark_task_completed(task_index)

        elif choice == "4":
            task_manager.save_tasks()

        elif choice == "5":
            print("Exiting Task Manager.")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
