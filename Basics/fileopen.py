# f=open('myfile.txt','a')
# # text = f.write("nice game")
# # print(text)
# # # f.close()
# with open('myfile.txt','a'):
#     f.write("i am within with")

f=open('myfile.txt', 'r')
i=0
while True:
    i=i+1
    line = f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"the marks of student {i} in maths is: {m1}")   
    print(f"the marks of student {i} in english is: {m2}") 
    print(f"the marks of student {i} in PS is: {m3}" )

    
