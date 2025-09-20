dictionary={}
while True:
    print("-"*50)
    print("")
    print("Welcome to the dictionary app! Here are your options.. \n1.Add/Update a word..\n2.Retrieve a word's definition\n3.Delete a word\n4.View all words\n5.Exit")
    choice=input("Enter your choice..")
    if choice=="1":
        key=input("What word would you like to add..?")
        value=input("what is the definition of the word..?")
        dictionary[key]=value
        print(f"The word {key} has been added sucessfully..!")

    elif choice=="2":
        retrieve=input("What word would you like to see..?")
        print(dictionary.get(retrieve,"YOUR NONEXISTENT WORD DOESNT EXIST.. TRY AGAIN!!"))
        """if retrieve in dictionary:
            print(dictionary[retrieve])
        else:
            print("YOUR NONEXISTENT WORD DOESNT EXIST.. TRY AGAIN!!")
"""
    elif choice=="3":
        delete=input("What word do you want to delete from the dictionary?")
        if delete in dictionary:
            del dictionary[delete]
        else:
            print("Word not available in dictionary..")

    elif choice=="4":
        view=input("Do you want to see all your words?")
        if dictionary:
            for i in dictionary:
                print(i,dictionary[i])
        else:
            print("There are no words in your dictionary to view...")

    elif choice=="5":
        print("Bye bye!! :)")
        break
    

