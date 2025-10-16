import random
matrix=[]
def boxuluu():
    for i in range(5):
        temp=[]
        for j in range(5):
            temp.append('-')
        matrix.append(temp)

    return matrix

def treasure():
    row=random.randint(0,4)
    column=random.randint(0,4)
    return(row,column) 

def hints(tr,tc,gr,gc):
    if gr<tr:
        return "MOVE DOWN!!"
    elif tr<gr:
        return "MOVE UP!!"
    elif gc<tc:
        return "MOVE RIGHT!!" 
    elif tc<gc:
        return "MOVE LEFT!!"
    

grid=boxuluu()
tr,tc=treasure()

print("WELCOME TO THE TREASURE HUNT GAME! PREPARE TO USE YOUR BRAIN!")
attempts=0
while True:
    print()
    for i in grid:
        print(" ".join(i))
    try:
        gr=int(input("Enter the row number from 0-4:"))
        gc=int(input("Enter the column number from 0-4:"))
    except ValueError:
        print("Invalid number, please enter a number from the options given earlier.:1")
        continue
    if gr not in range(5) or gc not in range(5):
        print("INVALID INPUT!! PLEASE ENTER A NUMBER FROM 0-4!!:")
        continue 

    if grid[gr][gc]=="x":
        print("This input was already entered.... please try another input:")
        continue
    if gr==tr or gc==tc:
        print("CONGRATULATIONS!!! YOU HAVE SUCCESSFULLY USED YOUR BRAIN AND FOUND THE TREASURE!!")
        break
    else:
        grid[gr][gc]=="x"
        hint=hints(tr,tc,gr,gc)
        print("HINT!",hint)
