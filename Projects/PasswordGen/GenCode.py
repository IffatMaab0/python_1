## Author : Iffat Maab
## Date   : 18th June 2025
## Description : Password Generator in Python

import string          ## Imports string module for predefined character sets
import random          ## import it for shuffling

##Predefined constants from the string module
s1=string.ascii_lowercase            
s2=string.ascii_uppercase            
s3=string.digits
s4=string.punctuation

plen=int(input("Enter the length of password: ")) 

# List to store all characters
s=[]       

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# Shuffle the character list from random module
random.shuffle(s)         

# Join the first 'plen' characters into a string
pswd= ("".join(s[0:plen])) 
print("Your Passwrod is: ", pswd)

            