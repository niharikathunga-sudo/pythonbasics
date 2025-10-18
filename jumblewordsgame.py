import random
words=["cake","biryani","laddoo","debate","laptop","noodles","waffles","boba"]
def mixed(word):
    wordlist=list(word)
    random.shuffle(wordlist)
    return "".join(wordlist)
def hints(word):
    return "The starting letter is {}".format(word[0])

score=0
rounds=4
print("WELCOME TO THE JUMBLING WORDS GAME!!💅🏽")
for i in range(1,5):
    firstword=random.choice(words)
    mixing=mixed(firstword)
    print(f"\nROUND {i}")
    print("Your scrambled word is..",mixing)

    hint=input("Do you want a hint?! yes or no..")
    if hint=="yes":
        print(hints(firstword))
    guess=input("What's your final guess? ")

    if guess==firstword:
        score+=1
        print("Congratulations, you guessed the correct answer!!")
    else:
        print("Sorry, that's not correct...")

print(f"GAME OVER! Your final score is....{score}/{rounds}")