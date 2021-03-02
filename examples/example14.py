import pandas as pd

data = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(data.head())
data = data.rename(columns={'Team':'Country'})
print(data.head())
medals = data['Medal'].value_counts()
print(medals)
city = data['City'].value_counts()
print(city)
country = data['Country'].value_counts()
print(country)
