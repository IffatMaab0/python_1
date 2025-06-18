## constructor is called whenver a object is initiated, and invoked it self
##obj attribute has higher percedence than class attribute
## variables of class are attributes
class student:
    def __init__(self, name, marks):          #parameterized constructor
        self.name = name
        self.marks = marks

    ## when self arguement is not required    
    @staticmethod                   
    def welcome():
        print("you are welcome!") 


    def avg_score(self):                      #method to calculate and display average
        sum = 0
        for value in self.marks:
            sum = sum + value
        print(f"{self.name}, your average score is {sum/3}")   
         

s1 = student("Leo", [97, 89, 91] )              #object created
s1.welcome()
s1.avg_score()                           #method called of stdent class
s2 = student("Maab", [87, 91, 98] )
s2.avg_score()
