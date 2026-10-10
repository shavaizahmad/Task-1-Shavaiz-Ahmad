import json
project1 = []
# Old tasks load karna
try:
    with open("tasks.json", "r") as file:
        project1 = json.load(file)

except FileNotFoundError:
    project1 = []
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(project1, file, indent=4)
    
while True:
    print("\n====Welcome In TO_DO List====\n")
    print("1- Add Task : ")
    print("2- View Task : ")
    print("3- Exit : ")

    try:
     choice = int(input("\nEnter Your Choice : "))
    except ValueError:
     continue

    if(choice == 1):

        user = input("\nEnter Your Task : ")

        task = {
            "id": len(project1) + 1,
            "task": user
        }

        project1.append(task)
        save_tasks()

        try:  
         choices = input("Do you want to add or view other task? (Y/N): ").lower()
        except ValueError:
           continue

        if choices == "n":
           print("\nTasks Added Successfuly")
           break



    elif(choice == 2):
      print("\n====Your Tasks=====")
     
      if len(project1) == 0:
            print("\nNo Tasks Available")
            continue
      
      for task in project1:
        print(task["id"], "-", task["task"])

      try:  
          choices = input("\nDo you want to add or view other task? (Y/N): ").lower()
      except ValueError:
          continue
        
      if choices == "n":
         print("\nTasks View Successfuly")
         break

    else:
       print("\nThanks for using To_Do List")
       break