# Name: Iffat Maab
# Date: 2025-06-17
# Description: A simple Python script to convert PKR to selected foreign currencies 
#              using exchange rates from a text file.

# Open the currency rate file and read all lines
with open('CurrencyRate.txt') as file:   
   lines=file.readlines()

# Create an empty dictionary to store currency name and rate
CurrDict={} 

# Split each line by tab and fill the dictionary  
for line in lines:
   parsed= line.split("\t")
   CurrDict[parsed [0]]= parsed[1]

# Get amount in PKR from user   
amount=int(input("Enter amount:"))

# Display all available currency options
print("Select the name of currency you want to convert this amount, Available options are:\n")
for item in CurrDict.keys():
   print(item)
   
# Get desired currency from user
currency=input("Enter name of Currency you want to exchange to: ") 
print(f"{amount} PKR is equal to {amount* float(CurrDict[currency])} of {currency}")  
