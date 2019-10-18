import pandas as pd
import numpy as np
from sklearn.cluster import k_means, KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv("C:/Users/Admin/Desktop/Titanic Data Set/train.csv")
test = pd.read_csv("C:/Users/Admin/Desktop/Titanic Data Set/test.csv")
# print("------------------------Training set --------------------------------------")
# print(train.describe())
# print("------------------------Test set ------------------------------------------")
# print(test.describe())
# # Missing values in train and test sets
# print("------------------------Missing values-------------------------------------")
# print("------------------------Training set --------------------------------------")
# print(train.isna().sum())
# print("------------------------Test set ------------------------------------------")
# print(test.isna().sum())
#
# Filling missing values in a column by its mean

train.fillna(train.mean(), inplace=True)
test.fillna(test.mean(), inplace=True)
#
# # Checking Again for missing values
# print("------------------------Missing values-------------------------------------")
# print("------------------------Training set --------------------------------------")
# print(train.isna().sum())
# print("------------------------Test set ------------------------------------------")
# print(test.isna().sum())

# print(train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived',
#                                                                                             ascending=False))

# removing trivial columns from the dataset
print(train.info())
train = train.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)
test = test.drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

# Converting non numerical column to numeric
le = LabelEncoder()
le.fit(test['Sex'])
le.fit(train['Sex'])
test['Sex'] = le.transform(test['Sex'])
train['Sex'] = le.transform(train['Sex'])
print(le.classes_)
print(train)
print(train.info())

# drop survived column
x = np.array(train.drop(['Survived'], 1).astype(float))
y = np.array(train['Survived'])
print("Value of X = {0}".format(x))

# using kmeans model


kmeans = KMeans(n_clusters=2, max_iter=600,
                algorithm='auto')  # You want cluster the passenger records into 2: Survived or Not survived

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(x)
kmeans.fit(X_scaled)

# #confidence
#
# z = np.array(test)
# print(confidence)

correct = 0
for i in range(len(x)):
    predict_me = np.array(x[i].astype(float))
    predict_me = predict_me.reshape(-1, len(predict_me))
    prediction = kmeans.predict(predict_me)
    # print(prediction)
    if prediction == y[i]:
        correct += 1

print(correct / len(x))
