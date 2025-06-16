def greet(fx):
    def mfx(*args, **kwargs):
        print("good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this function!")
    return mfx
def hello():
    print("Hello World!")        
@greet
def hello():
    print("Hello World!" )
def add(a,b):
    print(a+b)

hello() 
print("__NEXT FUNCTION!__")
greet(add)(1,2)   
