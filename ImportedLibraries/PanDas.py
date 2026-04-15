import numpy as np
import pandas as pd


###Series From List and Dictionary
# country = ["Pakistan", "India", "UAE"]
# print(pd.Series(country))        #index automatically generated
# mark = [75,65,82]
# sub= ["maths", "PS", "English"]
# marks = pd.Series(sub, index = mark, name = "Marks")
# print (marks)
# marks = {
#     "englihs": 78,
#     "maths": 85,
#     "PS": 74
# }
# dict_series = pd.Series(marks)

# csv reading
mov = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\bollywood.csv")
mov = mov.squeeze()
vk = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\kohli_ipl (1).csv")
vk= vk.squeeze()
sub = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\subs.csv")
sub = sub.squeeze()
# print(sub)

# print(sub.head(3))
# print(sub.tail(3))

# print(sub["lead"].value_counts())
# print(sub.sort_values(by = "lead" , ascending = False)).head(1).value[0] #function chaining
# print(vk.sort_values(ascending= False).head(1).value[0])

### Series with python functionalities
# print(len(sub))     #len, size , sorted(give output in list), min, max relational
import matplotlib.pyplot as plt
# plt.plot(sub)
# plt.show()
mov.value_counts("lead").head(20).plot(kind="bar")
plt.show()
