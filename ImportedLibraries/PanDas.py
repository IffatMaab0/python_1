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
import matplotlib.pyplot as plt
# plt.plot(sub)
# plt.show()
# mov.value_counts("lead").head(20).plot(kind="bar")
# plt.show()

###DATAFRAMES
# movies= pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\movies.csv")
# ipl = pd.read_csv(r"C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\ipl-matches.csv")
# student_dict = {'name':['a','b','c','d','e','f'],
#                 'iq':[100,80,120,70,0,0],
#                 'marks':[90,70,100,50,0,0],
#                 'package':[10,7,14,5,0,0]}
# student= pd.DataFrame(student_dict, columns=['name','iq','marks','package'])
# student.set_index('name', inplace=True)

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
#1->find all final winners
# val = ipl['MatchNumber'] =='Final'
# print(val)
# new_df= ipl[val]
# print(new_df)
# print(new_df[['Season','WinningTeam']])
#print(ipl[ipl['MatchNumber']=='Final'])[['Season','WinningTeam']] -->single line
#2->how many superover finishes occur
# print(ipl[ipl['SuperOver'] =="Y"].shape[0])
# print((ipl['SuperOver'] =="Y").sum())

#3->how many matches csk won in  kolkata
# print(ipl[(ipl['City']=='Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

#4-> match winner is toss winner in percentage
# print(((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0])/ipl.shape[0])*100)
#->movies with greater than 8 rating and votes >10000
# print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes']> 10000)])

#->5action movies with rating higher than 7.5
# cnd1 = movies['imdb_rating']> 7.5
# cnd2 = movies['genres'].str.split('|') .apply(lambda x:'Action' in x)  #str.contains('Action') 
# print(movies[cnd1 & cnd2 ].shape[0])

#->6 write a function that can return the track record of 2 teams against each other
# def match(team1, team2):
#     matches = ipl[
#         ((ipl['Team1'] ==  team1) & (ipl['Team2'] == team2))|
#         ((ipl['Team2'] == team1) & (ipl['Team2'] == team1))
#     ].sum()
#     team1_wins = (matches['WinningTeam'] == team1).sum()
#     team2_wins =(matches['WinningTeam'] == team2).sum()
#     print(team1, ':' ,team1_wins)
#     print(team2, ':' , team2_wins)

#     print("Total Matches", matches)
# match('Gujarat Titans', 'Rajasthan Royals')

#1-> find player which won most player of match in finals and qualifier
# ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts
#->2 toss decision
# ipl['TossDecision'].value_counts().plot(kind='pie')
# plt.show()


###GROUPBYDATA
#->find top3 genre by total earning
movies = pd.read_csv(r'C:\Users\City Computer\Desktop\VS\python\ImportedLibraries\imdb-top-1000.csv')
# print(movies.columns)
# print(movies.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))
#2-> find the genre based on highest average imbd rating
# print(movies.groupby('Genre')['IMDB_Rating'].mean().sort_values(ascending=False).head(1))
#->3 find director with more popularity
# print(movies.groupby('Director')['No_of_Votes'].sum().sort_values(ascending = False).head(1))
#->4 find highest rated movie of each genre
# movies.groupby('genre')['IMDB_Rating','']sort_values later.....
#->5 no of done by by each actor
# print(movies.columns)
# movies['Star1'].value_counts()
# print(movies.columns)
# movies.groupby('Star1')['Series_Title'].count.sort_value(ascending = False)
# groupby -> desired coulumn -> aggregate (sum etc)

#looping on groups
genres = movies.groupby('Genre')
for groups, data in genres
    print(type(groups), type(data))
