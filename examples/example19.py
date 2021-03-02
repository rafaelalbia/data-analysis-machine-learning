import pandas as pd

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(data.head())

newData = data.dropna()
print(newData.head())

null = data.isnull()
amount = data.isnull().sum()
# newAmount = data.isnull().sum() / len(data['ID']) * 100
# print(newAmount)

data['Medal'] = data['Medal'].fillna('None')
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Height'] = data['Height'].fillna(data['Height'].mean())
data['Weight'] = data['Weight'].fillna(data['Weight'].mean())

newAmount = data.isnull().sum() / len(data['ID']) * 100
print(newAmount)
