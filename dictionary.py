capitals={"USA":"Washington D.C",
          "India":"New Dehli",
          "Austrailia":"Canberra",
          "Belgium":"Brussels",
          "Indonesia":"Jakarta",
          "Japan":"Tokyo",
          "United Kingdom":"London",
          "Ireland":"Dublin"}
print(len(capitals))
print(capitals["United Kingdom"])
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print("-"*100)
for i in capitals:
    print(i,"=",capitals[i])
print("-"*100)
for i,j in capitals.items():
    print(i,j)

del(capitals["Ireland"])
print(capitals)
