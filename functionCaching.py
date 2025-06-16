import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*2

print(fx(5))
print(fx(2))
print(fx(7))
print(fx(8))
print("it would print faster")
print(fx(5))
print(fx(2))
print(fx(7))
print(fx(8))
print("it would take some time again")
print(fx(10))



