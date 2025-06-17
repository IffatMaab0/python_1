class Father:
    def speak(self):
        print("I speak wisdom.")

class Daughter(Father):       #parent class inherited
    def cry(self):
        print("I am emotionally weak.")

# Use it
s = Daughter()   
s.speak() #parent class method inherited 
s.cry()    #own method