import pandas as pd

alumns = {'name': ['Ricardo', 'Carlos', 'Lucas', 'Leandro', 'Kevin'],
         'grade': [4.7, 8, 5, 6, 6.8],
         'situation': ['Disapproved', 'Approved', 'Disapproved', 'Approved', 'Approved']}

dataFrame = pd.DataFrame(alumns)
print(dataFrame)
firstLines = dataFrame.loc[0:2]
print(firstLines)
newDataFrame = dataFrame.loc[dataFrame['grade'] >= 6]
print(newDataFrame)
otherNewDataFrame = dataFrame.loc[dataFrame['situation'] != 'Approved']
print(otherNewDataFrame)
