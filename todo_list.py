# To-Do List Project (Python - Console Based)
def todo_list():
    tasks = []

    def show_tasks():
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    while True:
        print("\nOptions: 1-Add, 2-Remove, 3-Show, 4-Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter task: ")
            tasks.append(task)
        elif choice == '2':
            show_tasks()
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
            else:
                print("Invalid number")
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    todo_list()
