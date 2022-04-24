import pandas
import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

table = pandas.read_csv("pakistan.csv")

columns=table.columns[1:len(table.columns)]
features=[]
for i in range(len(columns)):
    features.append(columns[i])

X=table[features]
y=table['Landslide']

TestSize=0.33
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=TestSize,random_state=7)


kfold=sklearn.model_selection.KFold(n_splits=10,shuffle=True,random_state=7)
type(kfold)


dtree=DecisionTreeClassifier(max_depth=7)

rforest=RandomForestClassifier(max_depth=7,n_estimators=1000)

trening = dtree.fit(X_train, y_train)
results = dtree.score(X_test, y_test)
print("Accuracy for 33% test split: ", results)

from sklearn.model_selection import cross_val_score

results=cross_val_score(dtree,X,y,cv=kfold)
print("CV:")
print(results.mean())
fresults=cross_val_score(rforest,X,y,cv=kfold)
print('CV Random Forest: {:.2f}'.format(fresults.mean()))

import imageio
im = imageio.imread('landslide0.png')
print(im[0])
