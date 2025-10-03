def load_tasks():
   try:
     with open("tasks.txt") as fin:
      while(task:= fin.readline()):
       tasks.append(task)
   except Exception as e:
     print(e)

def save_tasks():
  with open("tasks.txt",'w') as fout:
    for task in tasks:
      fout.write(task)

      
def add_task():
    task=input("Enter Your task: ")
    if(task in tasks):
        print("Already Exists!")
    else:
     tasks.append(task)
     print("Successfully Added.")
def show_tasks():
    if(tasks):
     for count,task in enumerate(tasks,start=1):
        print(f" {count}. {task}")
    else:
       print("You don't have any Tasks yet.")

def remove_task():
    if(tasks):
      show_tasks()
      task=input("Enter task to remove:- ")
      if(task in tasks):
       tasks.remove(task)
       print("Successfully Removed.")
      else:
       print("Task Does Not Exist.")
    else:
       print("You don't have any Tasks yet.")
def clear_tasks():
   if(tasks):
     tasks.clear()
     print("Successfully Cleared.")
   else:
      print("You don't have any Tasks yet.")

print("\n\t \t **** To-Do-List ****")

tasks=[]

while(True):
    print('\n')
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View All Tasks")
    print("4. Clear All Tasks")
    print("5. Exit")
    try:
     choice = int(input("Enter Your choice:- "))
    except Exception as e:
       print(e)
    else:
     match choice:
        case 1:
            add_task()
        case 2:
          remove_task()
        case 3:
          show_tasks()
        case 4:
          clear_tasks()
        case 5:
          save_tasks()
          print("Closing App...")
          break
        case _:
          print("Wrong Choice!")

 
 