import pandas as pd
import numpy as np

alumns = {'names': ['Ricardo', 'Carlos', 'Lucas', 'Leandro', 'Kevin'],
         'grade': [4.7, 8, 5, 6, 6.8],
         'situation': ['Disapproved', 'Approved', 'Disapproved', 'Approved', 'Approved']}

dataFrame = pd.DataFrame(alumns)
print(dataFrame)

print()

newObject = pd.Series([2, 6, 7, 5, 3])
print(newObject)

print()

array = np.array([2, 6, 3, 5, 4])
otherNewObject = pd.Series(array)
print(array)
print(otherNewObject)
