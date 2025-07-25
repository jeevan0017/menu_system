todo_list=[]

def show_menu():
    print("/n--- TO_DO LIST MENU---")
    print("1.view tasks")
    print("2.Add task")
    print("3.Remove task")
    print("4.Exit")

def view_tasks():
    if not todo_list:
        print("No tasks found.")
    else:
        for idx,task in enumerate(todo_list,1):
            print(f"{idx}.{task}")

def add_task():
    task=input("Enter a new task:")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def remove_task():
    view_tasks()
    try:
        task_num=int(input("Enter the task number to remove:"))
        removed=todo_list.pop(task_num-1)
        print(f"Task '{removed}' removed.")
    except(Indexerror,valueerror):
        print("Invalid task number.")

while True:
    show_menu()
    choice=input("Enter your choice(1-4):")

    if choice =='1':
        view_task()
    elif choice=='2':
        add_task()
    elif choice=='3':
        remove_task()
    elif choice=='4':
        print("Exiting...Goodbye!")
        break
    else:
        print("Invalid choice.please enter 1-4.")
