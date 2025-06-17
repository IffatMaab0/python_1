import re       # Importing the regular expressions module    

#Randomly generated text in which we want to find certain patterns
text = "I am learning Python and sometimes it is very hard to grab and sometimes some concepts are very easy to digest"

pattern = r"very\s+\w+"

#re.findall() built in funtion in re
matches = re.findall(pattern, text)

# Counting no. of times the pattern appears
count = len(matches)

#gives match object with more detail
full_matches = re.findall(r"very\s+\w+", text)
print("Sentences/parts containing 'very':")
for m in re.finditer(r"very\s+\w+", text):
    print("-", m.group())                     ## .group() returns the actual matched string

# Printing the total number of times 'very' is followed by another word
print(" 'Very' used", count, "times.")
