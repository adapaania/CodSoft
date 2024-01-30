"----To Do List Application----"
tasks=[]
    
def add_task():
    global tasks
    no=int(input("How many tasks do you want to add?: "))
    print()
    for i in range (no):
        task=str(input("Enter your task: "))
        tasks.append({"task":task,"completed":False})
    print()
    #taskdict={index+1:value for index,value in enumerate (tasks)}
    print("Task added successfully!")
    print()
    view(tasks)

def view(x):
    print("To Do List: ")
    for index, task in enumerate(x, start=1):
        status = "[ ]" if not task["completed"] else "[✓]"
        print(f"{index}. {status} {task['task']}")
    menu()

    
def update(x):
    print()
    comp=str(input("Have you completed any task? (y/n): "))
    if comp.lower()=="y":
        update=int(input("which task do you want to update?"))
        for index, task in enumerate(x, start=1):
            if update==index:
              task["completed"]=True
    view(x)
    print()
    menu()
        
    

def drop(x):
    rem=int(input("Which task do you want to remove?"))
    for index, task in enumerate(x, start=1):
        if rem==index:
            x.pop(index-1)
    print("Deleted Task.")
    view(x)
    menu()
  

def exit_():
    op=str(input("Are you sure you want to exit? (y/n)"))
    if op.lower()== 'y':
        print("Thank You!")
        exit
    elif op.lower()=='n':
        menu()
    else:
        print("Please enter either y/n !")
  
def menu():
    print()
    print(""" To Do List:
                1. Add a Task
                2. Update Task
                3. Remove a Task 
                4. Exit
          """)
    choice = int(input("Enter your choice: "))
    print()
    while True:
        if choice == 1:
            add_task()
        elif choice == 2:
            update(tasks)
        elif choice == 3:
            drop(tasks)
        elif choice == 4:
            exit_()
            break
        else:
            print("You have entered the wrong choice. Please input either 1,2,3, or 4.")
    
menu()









    
                       
