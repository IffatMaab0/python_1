## polymorphism--->operator overloading

class complex:
    def __init__(self, real,img):
        self.real=real
        self.img=img
    def showNumb(self):
        print(f"{self.real}i + {self.img}j")
    ##dunder method
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg=self.img + num2.img
        return complex(newReal, newImg)
num1=complex(1,3)   
num1.showNumb()
num2=complex(5,3)
num2.showNumb()

Added=num1 + num2
Added.showNumb()
