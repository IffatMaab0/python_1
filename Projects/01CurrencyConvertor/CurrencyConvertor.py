
# Description: A simple Python script to convert PKR to selected foreign currencies 
        ##   using exchange rates from a text file.


with open('CurrencyRate.txt') as file:   
   lines=file.readlines()

CurrDict={} 

# Split each line by tab and fill the dictionary  
for line in lines:
   parsed= line.split("\t")
   CurrDict[parsed [0]]= parsed[1]

## amount in PKR  
amount=int(input("Enter amount:"))


print("Select the name of currency you want to convert this amount, Available options are:\n")
for item in CurrDict.keys():
   print(item)
   

currency=input("Enter name of Currency you want to exchange to: ") 
print(f"{amount} PKR is equal to {amount* float(CurrDict[currency])} of {currency}")  
