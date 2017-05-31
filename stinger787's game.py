import random

noob = random.randint(4, 6)#variable
beast = random.randint(1, 3)#variable


#DICE CHECK
print("you rolled "+ str(noob))
print ("da beast rolled "+ str(beast))

if noob > beast:
    print("you won")
elif noob < beast:
    print("you lost")
    



