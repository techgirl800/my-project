"""A command-line to-do list that saves tasks in a JSON file."""

import json
from pathlib import Path


TASKS_FILE = Path(__file__).with_name("tasks.json")


def load_tasks(file_path=TASKS_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks, file_path=TASKS_FILE):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(tasks, title):
    next_id = max((task["id"] for task in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True
    return False


def delete_task(tasks, task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return True
    return False


def show_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return

    print("\nYour tasks:")
    for task in tasks:
        status = "Done" if task["completed"] else "Not done"
        print(f'{task["id"]}. [{status}] {task["title"]}')


def main():
    tasks = load_tasks()
    menu = "\nTo-Do List\n1. Add task\n2. View tasks\n3. Complete task\n4. Delete task\n5. Quit"

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Task: ").strip()
            if title:
                task = add_task(tasks, title)
                save_tasks(tasks)
                print(f'Task {task["id"]} added.')
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice in ("3", "4"):
            try:
                task_id = int(input("Task number: "))
            except ValueError:
                print("Enter a valid task number.")
                continue

            changed = complete_task(tasks, task_id) if choice == "3" else delete_task(tasks, task_id)
            if changed:
                save_tasks(tasks)
                print("Task completed." if choice == "3" else "Task deleted.")
            else:
                print("Task not found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Choose a number from 1 to 5.")


if __name__ == "__main__":
    main()