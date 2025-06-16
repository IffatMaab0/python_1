list1=["What is capital of Pakistan?","Which planet is known as Red Planet?","Which is the smallest prime number?","How many continents are there in the world?","Which animal is known as the King of the Jungle?"]   
list2=["islamabad", "mars","two","seven","lion"] 
amount=0
for i in range(len(list1)):
    print(list1[i])
    for char in range(len[list2]):
        print(list2[char])
    a=input("enter answer (1-5) ")
    if(a==(char+1)):
        print("excellent!")
        amount +=1000
    else:
        print("Incorrect!")  
print("Final amount: ",amount)          


