import pandas as pd

archive = pd.read_excel('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/archive.xlsx')
print(archive.head())

athleteEvents = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/athlete_events.csv')
print(athleteEvents.head(15))
