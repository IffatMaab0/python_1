
## Description : Password Generator in Python

import string          
import random          


s1=string.ascii_lowercase            
s2=string.ascii_uppercase            
s3=string.digits
s4=string.punctuation

plen=int(input("Enter the length of password: ")) 


s=[]       

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

# Shuffle the character list from random module
random.shuffle(s)         


pswd= ("".join(s[0:plen])) 
print("Your Passwrod is: ", pswd)

            