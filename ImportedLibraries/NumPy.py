import numpy as np
# a1 = np.arange(0,12).reshape(3,4)
# a2 = np.arange(4,28,2).reshape(3,4)
# print(a1, a2, sep="\n")
# #must be of same shape
# a3=a1+a2
# print(a3)

###numpy functions -->log exponent trignomatry dot product
# np.round(np.random.random((2,3))*100)
# np.floor(np.random.random((2,3))*100)
# np.ceil(np.random.random((2,3))*100)

### indexing -->1 elementat a time;  Slicing-->multiple items at a time
# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(8).reshape(2,2,2)

# print(a2[2,3])
# print(a3[0,0,1])    #0 ->first array; 0-> first row of that array; 1->second column

# print(a1[2:5])  #from 2-4
# print(a2)
# print(a2[0:2,1:3])
# print(a2[0::2, 0::3])  #-->> corners
# print(a2[0::2, 1::2])
# print(a2[1, 0::3])
# print(a2[0:2, 1:])

# a3 = np.arange(27).reshape(3,3,3)
# print(a3)
# print("slicing")
# print(a3[1,:,: ])     #a3[1]
# print(a3[::2])
# print(a3[0,1])
# print(a3[2, 1:, 1:])
# print(a3[0::2, 0, 0::2])

#iterating
# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(27).reshape(3,3,3)
# for i in np.nditer(a3):       #if not used it will print 1d array and then 2nd and then 3rd
#     print (i)                   #nditer first convert to 1d array

#Reshaping(transpose, ravel)
# a2 = np.arange(12).reshape(3,4)
# print(a2)
# print (np.ravel(a2))   #-->convert to 1d array

#Stacking                         #shape must be same
# a4 = np.arange(12).reshape(3,4)
# a5= np.arange(12,24).reshape(3,4)
# a6 =np.hstack((a5,a4))
# print(a6)

#Splitting   must be equal
# print(np.hsplit(a4, 2))
# print(np.vsplit(a4,3))   #each part is stilld array
