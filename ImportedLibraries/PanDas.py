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
# mov = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\bollywood.csv")
# mov = mov.squeeze()
# vk = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\kohli_ipl (1).csv")
# vk= vk.squeeze()
# sub = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\subs.csv")
# sub = sub.squeeze()
# print(sub)

# print(sub.head(3))
# print(sub.tail(3))

# print(sub["lead"].value_counts())
# print(sub.sort_values(by = "lead" , ascending = False)).head(1).value[0] #function chaining
# print(vk.sort_values(ascending= False).head(1).value[0])

### Series with python functionalities
# print(len(sub))     #len, size , sorted(give output in list), min, max relational
# import matplotlib.pyplot as plt
# plt.plot(sub)
# plt.show()
# mov.value_counts("lead").head(20).plot(kind="bar")
# plt.show()

###DATAFRAMES
movies= pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\movies.csv")
ipl = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\ipl-matches.csv")
student_dict = {'name':['a','b','c','d','e','f'],
                'iq':[100,80,120,70,0,0],
                'marks':[90,70,100,50,0,0],
                'package':[10,7,14,5,0,0]}
student= pd.DataFrame(student_dict, columns=['name','iq','marks','package'])
student.set_index('name', inplace=True)

# print(movies)
# print(movies.describe())
# print(movies.info())
# print(movies.duplicated().sum())

##selecting cols
# print(movies['title_x'])   #series
# print(movies[['title_x','year_of_release','runtime' ]])   #dataframe
# print(ipl[['Team1','Team2','WinningTeam']])
##selecting rows
# print(movies.iloc[0:5])
# print(student.loc["a"])
# print(student.loc['a':'c'])
#indexing position ->iloc
#index name ->loc   but still default index could be used

##selecting both rows and cols
# print(movies.iloc[0:3,0:3])

###filtering DataFrame
#1-find all final winners
# val = ipl['MatchNumber'] =='Final'
# print(val)
# new_df= ipl[val]
# print(new_df)
# print(new_df[['Season','WinningTeam']])
#print(ipl[ipl['MatchNumber']=='Final'])[['Season','WinningTeam']] -->single line
#2-


