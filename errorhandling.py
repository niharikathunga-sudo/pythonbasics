"""try:
    number=int(input("Enter a number.."))
    result=10/number
    print(result)

except ZeroDivisionError:
    print("You can not divide a number by zero...")

except ValueError:
    print("Enter a valid number only like 1,2,3,4,etc....")"""


print("Welcome to the Safe Calculator app!!")
while True:
    try:
        number1=int(input("Enter your first number..."))
    except ValueError:
        print("Enter a valid number only like 1,2,3,4,etc....")
        continue

    try:
        number2=int(input("Enter your second number..."))
    except ValueError:
        print("Enter a valid number only like 1,2,3,4,etc....")
        continue

    operation=input("Enter your operation choice...(+.-,*,/)")
    try:
        if operation=="+":
            print(number1+number2)

        elif operation=="-":
            print(number1-number2)

        elif operation=="*":
            print(number1*number2)

        elif operation=="/":
            print(number1/number2)
    
        else:
            print("Please enter a valid operater and try again..")
    
    except ZeroDivisionError:
        print("You can not divide a number by zero...")
        continue
    repeat=input("Would you like to preform another calculation..? yes or no: ")
    if repeat=="yes":
        continue
    else:
        break

