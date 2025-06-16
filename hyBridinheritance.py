class Mother:
    def cook(self):
        print("I cook delicious food.")

class Father:
    def work(self):
        print("I work to earn.")

class Daughter(Mother, Father):  
    def copyy(self):
        print("I try to copy good habits from my parents.")
c = Daughter()
c.cook()  
c.work()  
c.copyy()   
