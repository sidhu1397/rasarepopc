import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import sklearn.metrics as sm

train = pd.read_csv("C:/Users/Admin/Desktop/Titanic Data Set/train.csv")
test = pd.read_csv("C:/Users/Admin/Desktop/Titanic Data Set/test.csv")


train.fillna(train.mean(), inplace=True)
test.fillna(test.mean(), inplace=True)

train = train.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)
test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# print(train)
# print(test)


le = LabelEncoder()
le.fit(test['Sex'])
le.fit(train['Sex'])
test['Sex'] = le.transform(test['Sex'])
train['Sex'] = le.transform(train['Sex'])
print(le.classes_)
print(train)
print(train.info())

x = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])

cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(x)
cluster.fit_predict(X_scaled)
print(sm.accuracy_score(y,cluster.labels_))