from datetime import datetime
class Task:
    def __init__(self, task_name, task_description, task_date):
        self.task_name = task_name
        self.task_description = task_description
        self.task_date = task_date
        self.completed = False
    def __str__(self):
        status = "Completed"if self.completed else"Not Completed"
        return f"task_name: {self.task_name}, task_description: {self.task_description}, task_date: {self.task_date},status:{status}"
    
class To_Do_List:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, task_description, task_date):
        task=Task(task_name, task_description, task_date)
        self.tasks.append(task)
        
       
        
    def complete_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                task.completed = True
                print(f"task is completed")
                break
            else:
                print(f"task is not found")
               
               

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.task_name == task_name:
                self.tasks.remove(task)
                print(f"task is removed")
                break
            else:
                print(f"task is not found")  
            
    def sort_tasks(self):
       self.tasks.sort(key=lambda x: (x.completed, x.task_date))

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found")
        else:
             for task in self.tasks:
                 print(task)
                 
todo_list=To_Do_List()
while True:
    print("To_D0_List ")
    print("1.Add task")
    print("2.Complete task")
    print("3.Remove task")
    print("4.Sort tasks")
    print("5.Display tasks")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        task_name=input("Enter task name:")
        task_description=input("Enter task description:")
        priority=int(input("Enter task priority:"))
        task_date=input("Enter task date:")
        todo_list.add_task(task_name,task_description,task_date)
        print("task addeed successfully")
    elif choice==2:
        task_name=input("Enter task name:")
        todo_list.complete_task(task_name)
    elif choice==3:
        task_name=input("Enter task name:")
        todo_list.remove_task(task_name)
    elif choice==4:
        todo_list.sort_tasks()
    elif choice==5:
        print("Your tasks")
        todo_list.display_tasks()
    elif choice==6:
        print("Thanks for using a To Do List")
        break
    else:
         print("Your chice is not existing in the menu")