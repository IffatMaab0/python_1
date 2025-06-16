import re

text = "I am learning Python and sometimes it is very hard to grab and sometimes some concepts are very easy to digest"

pattern = r"very\s+\w+"

matches = re.findall(pattern, text)
count = len(matches)
full_matches = re.findall(r"very\s+\w+", text)
print("Sentences/parts containing 'very':")
for m in re.finditer(r"very\s+\w+", text):
    print("-", m.group())

print(" 'Very' used", count, "times.")
