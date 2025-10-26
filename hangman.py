import random
list=["nitendo","videogames","sackboy","astro","clash","brawl","spiderman"]
secret=random.choice(list)
guessed=["_"]*len(secret)
maxattempts=4
attempt=0
allguess=[]

print("Welcome to the Hangman game.. make sure to guss one letter at a time...")
print("word:"," ".join(guessed))

while attempt<maxattempts and "_" in guessed:
    print()
    letter=input("Enter a letter..").lower()

    if len(letter)!=1 or not letter.isalpha():
        print("This input is invalid, please try again and only enter one letter....")
        continue

    if letter in allguess:
        print("This letter has already been guessed... try again..")
        continue


    allguess.append(letter)
    
    if letter in secret:
        print(f"Good job! The letter {letter} is part of this word!!")
        
        for i in range(len(secret)):
            if secret[i]==letter:
                guessed[i]=letter

    else:
        attempt+=1
        print(f"Wrong guess! You have {maxattempts-attempt} attempts left!")
    
    print("word:"," ".join(guessed))
    print("Guessed letters are:"," ,".join(allguess))

if "_" not in guessed:
    print(f"Congratulations! You have guessed the word {secret} successfully!")

else:
    print(f"GAME OVER!! You lost :(.. the correct word was {secret}..)")