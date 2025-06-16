def apply(fx ,value):
    return fx(value) * fx(value)
double = lambda x: x*x
print(double(5))
print(apply(lambda x: x*x, 2))
