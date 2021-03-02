import pandas as pd

alumns = {'names': ['Ricardo', 'Carlos', 'Lucas', 'Leandro', 'Kevin'],
         'grade': [4.7, 8, 5, 6, 6.8],
         'situation': ['Disapproved', 'Approved', 'Disapproved', 'Approved', 'Approved']}

dataFrame = pd.DataFrame(alumns)
print(dataFrame)
print(dataFrame.shape)
print(dataFrame.describe())
