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

### iterating
# a1 = np.arange(10)
# a2 = np.arange(12).reshape(3,4)
# a3 = np.arange(27).reshape(3,3,3)
# for i in np.nditer(a3):       #if not used it will print 1d array and then 2nd and then 3rd
#     print (i)                   #nditer first convert to 1d array

### Reshaping(transpose, ravel)
# a2 = np.arange(12).reshape(3,4)
# print(a2)
# print (np.ravel(a2))   #-->convert to 1d array

### Stacking                         #shape must be same
# a4 = np.arange(12).reshape(3,4)
# a5= np.arange(12,24).reshape(3,4)
# a6 =np.hstack((a5,a4))
# print(a6)

#Splitting must be equal
# print(np.hsplit(a4, 2))
# print(np.vsplit(a4,3))   #each part is still same dimension array as before


### NumpyArray Vs PythonLists 
          #Speed & Convenience
# import time          
# a= [i for i in range(10000000)]
# b=[i for i in range(10000000,20000000)] 
# c =[]
# start = time.time()
# for i in range(len(a)):
#     c.append(a[i]+ b[i])   
# timeTaken= time.time() - start 
# print ("TimeTaken by Lists: ", timeTaken)      

# d= np.arange(10000000)
# e = np.arange(10000000,20000000)
# start2 = time.time()
# c= d+e
# timeTaken2= time.time() - start2
# print("TimeTaken by numpy: ", timeTaken2)
        #Memory
# import sys        
# a = np.arange(1000000, dtype= np.int32)   
# print(sys.getsizeof(a))     

### Advance/Fancy Indexing  -->when unable to build pattern via normal indexing
# a = np.arange(24).reshape(6,4)
# print(a[[0,2,3,5]])
# print(a[[0,1,3,4]])
# print(a[:, [0,1,3,4]])  ---> for columns


    ###BoleanIndexing   --> for specific output
# a = np.random.randint(1,100,24).reshape(6,4) 
# print(a) 
#--> find numb greater than 50
# print(a[a>50])
#-->find even numb
# print(a[a%2 ==0])
# #--> even and greater than 50
# print(a[(a>50) & (a%2==0)])
# #--> find all divisible of 7
# print(a[a%7 ==0])      #for not divisible print(~(a[a%7 ==0]))

### Broadcasting
# a= np.arange(12).reshape(3,4)
# b= np.arange(3)
# print(a+b)   --> for (4,3)
# print(a+b)  
# a= np.arange(3).reshape(3,1)
# b= np.arange(3,6).reshape(1,3)
# print(a+b)
# a= np.arange(3).reshape(1,3)
# b= np.arange(4).reshape(4,1)
# print(a+b)
# a= np.arange(16).reshape(4,4)
# b= np.arange(4).reshape(2,2)
# print(a+b)

### working with mathematical formulas
# --> Sigmoid
# def sigmoid(array):
#     return 1/(1+ np.exp(-(array)))
# a= np.arange(100)
# print(sigmoid(10))
# -->Mean Squared Error
# actual = np.random.randint(1,50,25)
# predicted = np.random.randint(1,50,25)
# def mse(actual,predicted):
#     return np.mean((actual-predicted)**2)
# print(mse(actual,predicted))

### Working with missing values np.nan
# a = np.array([1,2,3,4,5,np.nan, 7])
# print(a)
# print(np.isnan(a))  #-->bolean array
# print(a[~np.isnan(a)])

### plotting Graph
# import matplotlib.pyplot as plt
#   # -> plotting 2d graph
# #--> x=y
# x= np.linspace(-10, 10, 100)  
# # y = x                            #shape of x and y must be same


# plt.plot(x,y)           # we have to use linspace otherwise the point s on graph would 
# plt.show()               # be problematic
#-->y = x**2
# y = x**2
# plt.plot(x,y)
# plt.show()
#-->y=sin(x)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()
# --> y = xlog(x)
# y = x * (np.log(x))
# plt.plot(x,y)
# plt.show()
#    plotting scatter plot

