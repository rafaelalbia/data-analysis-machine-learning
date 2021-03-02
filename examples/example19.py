import pandas as pd

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(data.head())

newData = data.dropna()
print(newData.head())

null = data.isnull()
amount = data.isnull().sum()
newAmount = data.isnull().sum() / len(data['ID']) * 100
print(newAmount)

print(data['Medal'].fillna('None'))
print(data['Age'].fillna(data['Age'].mean()))
print(data['Height'].fillna(data['Height'].mean()))
print(data['Weight'].fillna(data['Weight'].mean()))
