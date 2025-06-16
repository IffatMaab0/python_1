class Father:
    def speak(self):
        print("I speak wisdom.")

class Daughter(Father): 
    def cry(self):
        print("I am emotionally weak.")

# Use it
s = Daughter()
s.speak()  
s.cry()   