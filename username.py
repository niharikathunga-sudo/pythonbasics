import random
while True:
    fullname=input("Enter your full name.. [exit to quit...]")
    if fullname=="exit":
        break
    nameparts=fullname.split()
    if len(nameparts)<2:
        print("Please enter your first and last name..")
        continue
    else:
        first=nameparts[0]
        last=nameparts[1]
        username1=first+last
        username2=first[:3]+last[:-3]
        username3=first[:-3]+last[:-2]
        randomnum= random.randint(0,99)
        username4=first+str(randomnum)
        username5=last+str(randomnum)
        username6=first[:2]+last[:-3]+str(randomnum)
        user=[username1,username2,username3,username4,username5,username6]
        randomusername=random.choice(user)
    print(randomusername)
    print("-"*40)