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