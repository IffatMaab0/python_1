class Grandfather:            
    def farm(self):
        print("I owe a farm.")

class Father(Grandfather):
    def car(self):
        print("I drive a car.")

class Daughter(Father):
    def laptop(self):
        print("I owe a laptop.")

# Use it
s = Daughter()
s.farm()       #inherited from first parent    
s.car()        
s.laptop() 