import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(data.head())

male = data.loc[data['Sex'] == 'M']

heightMale = male['Height']
weightMale = male['Weight']

plt.scatter(heightMale, weightMale)
plt.show()
