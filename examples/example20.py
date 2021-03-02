import pandas as pd

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/wine_dataset.csv')
print(data.head())

data['style'] = data['style'].replace('red', 0)
data['style'] = data['style'].replace('white', 0)
print(data.head())

target = data['style']
build = data.drop('style', axis = 1)
