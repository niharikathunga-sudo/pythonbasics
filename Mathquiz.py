import random
num1=random.randint(1,20)
num2=random.randint(1,20)
chances=3
restart=False
while chances>0:
  print(f"What is {num1}+{num2}?")
  guess=int(input())
  if guess==num1+num2:
    print("You got it right")
    restart=True
  else:
    print("Try again..")
    chances-=1
  if chances==0:
    print("You LOST..?!")
    restart=True
  if restart==True:
    retry=input("DO U WANT TO PLAY AGAINNNN??  Yes or Nah")
    if retry.lower()=="yes":
      chances=3
      num=random.randint(1,20)
      restart=False
      continue
    else:
      print("Thank you for playing but please don come back ever again!!:)")