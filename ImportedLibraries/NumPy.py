import numpy as np
a1 = np.arange(0,12).reshape(3,4)
a2 = np.arange(4,28,2).reshape(3,4)
print(a1, a2, sep="\n")
#must be of same shape
a3=a1+a2
print(a3)

