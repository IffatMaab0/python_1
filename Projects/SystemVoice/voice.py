## This Python script uses the pyttsx3 library to collect a list of names from user input and then provides a spoken "shoutout" for each name using text-to-speech.
  ## provides a spoken "shoutout" for each name using text-to-speech.
  
import pyttsx3 as py

names = []
while True:
    name = input("Enter a name or quit to quit: ")
    if name.lower() == 'quit':
        break
    names.append(name)

for name in names:
    engine = py.init()
    print(f"Shoutout to {name}")
    engine.say(f"Shoutout to {name}")
    engine.runAndWait()