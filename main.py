
def load_tasks(filename='tasks.txt'):
    try:
        with open(filename, 'r') as file:
            tasks = [eval(line.strip()) for line in file]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    for index, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Pending"
        print(f"{index + 1}. {task['description']} - Status: {status}")

def add_task(tasks):
    description = input("Enter task description: ")
    task = {
        'description': description,
        'completed': False
    }
    tasks.append(task)
    print("Task added!")

def remove_task(tasks):
    task_number = int(input("Enter task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task removed!")
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    task_number = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")


# Main program
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
