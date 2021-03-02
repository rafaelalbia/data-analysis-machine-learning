import pandas as pd

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(data.head())

data = data.drop('NOC', axis = 1)
print(data.head())
