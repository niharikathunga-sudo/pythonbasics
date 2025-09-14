dictionary={}
while True:
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
    





