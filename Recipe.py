def ctg(cup,ingredient):
    measurements={"flour":120,"sugar":200,"butter":230}
    if ingredient in measurements:
        grams=cup*measurements[ingredient]
        return grams 
    else:
        print("This ingredient is not available in the system....")

def gtc(grams,ingredient):
    measurements={"flour":120,"sugar":200,"butter":230}
    if ingredient in measurements:
        cup=grams/measurements[ingredient]
        return cup 
    else:
        print("This ingredient is not available in the system....")

def tabletotea(tablespoons):
    return tablespoons*3

def teatotable(teaspoons):
    print(teaspoons/3)

while True:
    print("-"*50)
    print()
    print("Welcome!! Here are your options to begin..\n1.Convert cups to grams\n2.Convert grams to cups\n3.Convert tablespoons to teaspoons\n4.Convert teaspoons to tablespoons\n5.Exit")
    choice=input("What would you like to do (1-5)..?")
    if choice=="1":
        ingredient=input("What ingredient would you like to convert..?")
        cups=int(input("What number of cups would you like to convert..?"))
        result=ctg(cups,ingredient)
        print(f"result:{result}grams")
 
    if choice=="2":
        ingredient=input("What ingredient would you like to convert..?")
        grams=int(input("What number of grams would you like to convert..?"))
        result=round(gtc(grams,ingredient),2)
        print(f"result:{result}cups")

    if choice=="3":
        ingredient=("What ingredient would you like to convert..?")
        tablespoons=int(input("What number of tablespoons would you like to convert..?"))
        result=tabletotea(tablespoons)
        print(f"result:{result}teaspoons")

    if choice=="4":
        ingredient=("What ingredient would you like to convert..?")
        teaspoons=int(input("What number of teaspoons would you like to convert..?"))
        print("result in tablespoons is..")
        round(teatotable(teaspoons),2)
        

    if choice=="5":
        print("Thank you for using our program! Bye Bye! :)")
        break


