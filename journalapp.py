from datetime import datetime
def add_entry():
    add=input("What would u like to write in your journal?")
    with open("n.txt","a") as file:
        file.write(add+"\n")
    print("Entry saved..")
def view_entry():
    with open("n.txt","r") as file:
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i,j in enumerate(file,1):
            print(date,i,j)
while True:
    print("--- Journal App ---\n1.Add an entry\n2.View an entry\n3.Exit")
    choices=input("Enter your choice..")
    if choices=="1":
        add_entry()

    if choices=="2":
        view_entry()

    if choices=="3":
        print("Goodbye!")
        break

