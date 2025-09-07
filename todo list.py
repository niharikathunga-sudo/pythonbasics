tasks=[]
while True:
    print( "---To Do List Menu---\n1.View Tasks\n2.Add a task\n3.Remove a task\n4.Exit" )
    menu=input("Choose an option 1-4.... ")
    if menu=="1":
        if not tasks:
            print("Your to-do list is empty...")
        else:
            for i,j in enumerate (tasks,1):
                print(i,j)
    elif menu=="2":
        addtask=input("What task whould you like to add to your list..? ")
        tasks.append(addtask)
        print(addtask+" has been added to tasks..")

    elif menu=="3":
        removetask=input("What task is getting removed from your to-do list..?")
        if removetask.isdigit():
            index=int(removetask)-1
            if index>=0 and index<len(tasks):
                tasks.pop(index)
                print(f"Task {removetask} successfully removed..!")
            else:
                print("Invalid task number..")    
        else:        
            if removetask in tasks:
                tasks.remove(removetask)
                print(f"Task {removetask} successfully removed..!")
            else:
                    print("Task not in list...try again..")

    elif menu=="4":
        print("Exiting....")
        break

