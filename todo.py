tasks = []
#lists grow and shrink dynamically

def show_menu():
    print("\nTo Do List")
    print()
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    #input pauses and waits for user input
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("\nTasks:")
    print()
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    #f string allows to use variables 

def delete_task():
    view_tasks()
    if not tasks:
        return
    task_number=input("Enter task number to delete: ")
    if not task_number.isdigit():
    #isdigit checks if input contains only numbers or not
        print("Invalid input")
        return
    task_number=int(task_number)
    if task_number<1 or task_number>len(tasks):
    #check valid range
        print("Task number is out of range")
        return
    removed_task=tasks.pop(task_number-1)
    #-1 because python lists start from 0
    print(f"Removed task {removed_task}")

    
while True:
    show_menu()
    choice=input("Choose an option (1-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Peace Out!!")
        break
    else:
        print("Invalid choice. Try again")
        
    

