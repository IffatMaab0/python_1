s={}
print(type(s))
se=set()
print(type(se))
see={2,4,5,7,8}
#accessing values of set
for value in see:
    print(value)
s1={2, 4, 6, 7, 1}
s2={2,3,4,1,9,6}
print("the intersection is: ",s1.intersection(s2))
print("the union is: ", s1.union(s2))
s1.update(s2)
print(s1, s2)
print(s1.intersection_update(s1))