import random
def check(comp, user):
    if comp==user:
        return 0
    if (comp == 0 and user == 1):
        return -1
    if(comp==2 and user==0):
        return -1
    if(comp==1 and user==2):
        return -1
    return 1               
user = int(input("choose '0' for Snake, '1' for water and '2' for Gun > "))
if(user<0 and user> 2):
    print("Invalid Choice!")
    exit(0)
comp = random.randint(0,2)
print("you choose > ", user)
print("Machine choose > ", comp)
score= check(comp,user)
if(score==0):
    print("its Draw!")
elif(score == -1):
    print("You lose!")
else:
    print("You Won!")
