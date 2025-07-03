
# Description: A simple Python console game where the user competes against the computer using random choices.

import random

# Function to check who wins
def check(comp, user):
    if comp==user:
        return 0    #Draw
    if (comp == 0 and user == 1):
        return -1                ## Snake drinks water (comp wins)
    if(comp==2 and user==0):
        return -1                 # Gun kills snake (comp wins)
    if(comp==1 and user==2):
        return -1                    # Water drowns gun (comp wins)
    
    return 1                         # Otherwise, user wins

user = int(input("choose '0' for Snake, '1' for water and '2' for Gun > "))
if(user<0 and user> 2):
    print("Invalid Choice!")
    exit(0)
    
# Computer randomly chooses
comp = random.randint(0,2)

#Show Choice
print("you choose > ", user)
print("Machine choose > ", comp)

score= check(comp,user)
if(score==0):
    print("its Draw!")
elif(score == -1):
    print("You lose!")
else:
    print("You Won!")
