import json
file_name = "tasks.json"
#tasks get saved here permanently

tasks = []
#lists grow and shrink dynamically


def load_tasks():
    global tasks
    #global used as it will update our main "tasks" list
    try:
        with open(file_name, "r") as f:
        #file opened in read mode
            tasks = json.load(f)
        if not isinstance(tasks, list):
            tasks=[]
            #reset if the file has something but a list
    except FileNotFoundError:
        tasks=[]
        #create a file if doesnt exist
    except json.JSONDecodeError:
        tasks=[]
        #file exists but corrupted or empty invalid json, reset it

def save_tasks():
    with open(file_name, "w") as f:
    #opened file in write mode
        json.dump(tasks, f, indent=2)
        #json.dump writes python objects into JSON text
        #indent is basically indentation
    


def show_menu():
    print("\nTo Do List")
    print()
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete a Task")
    print("5. Exit")

# def add_task():
#     task = input("Enter a new task: ")
#     #input pauses and waits for user input
#     tasks.append(task)
#     print("Task added successfully")

def add_task():
    title=input("Enter a new task: ").strip()
    if title=="":
        print("Task cannot be empty")
        return
    task={
        "title": title,
        "done": False   #default
    }
    #tasks are now dictionaries, not strings
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("No tasks found!")
        return
    for index, task in enumerate(tasks, start=1):
       status="✅" if task["done"] else "❌"
       print(f"{index}.{status} {task['title']}")

def mark_task():
    view_tasks()
    if not tasks():
        return
    choice = input("Enter task number to mark as done: ")
    if not choice.isdigit():
        print("Invalid input")
        return
    choice=int(choice)
    if choice < 1 or choice > len(tasks):
        print("Task number out of range")
        return
    tasks[choice-1]["done"]=True
    save_tasks()
    print("Task marked as done")


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

load_tasks()


    
while True:
    show_menu()
    choice=input("Choose an option (1-4): ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Peace Out!!")
        break
    else:
        print("Invalid choice. Try again")
        
    

