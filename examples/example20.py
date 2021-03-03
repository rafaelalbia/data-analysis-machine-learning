import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

archive = pd.read_csv('~/Documents/Workspace/Projects/data_analysis_machine_learning/examples/wine_dataset.csv')

print(archive.head())

archive['style'] = archive['style'].replace('red', 0)
archive['style'] = archive['style'].replace('white', 0)

x = archive['style']
y = archive.drop('style', axis = 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

x_train = x_train.values.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)

model = ExtraTreesClassifier(n_estimators=100)
model.fit(x_train, y_train)

result = model.score(x_train, y_train)
print("Accuracy: ", result)
