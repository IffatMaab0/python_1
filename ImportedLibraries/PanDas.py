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
sub = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\bollywood.csv")
sub = sub.squeeze()
# print(sub)

# print(sub.head(3))
# print(sub.tail(3))

# print(sub["lead"].value_counts())
# eror print(sub.sort_values(by = "lead" , ascending = False)).head(1).value[0] #function chaining