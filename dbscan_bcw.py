import numpy as np
from sklearn import preprocessing, neighbors, model_selection, svm
import pandas as pd
from sklearn.cluster import DBSCAN
import sklearn.metrics as sm
from sklearn.preprocessing import MinMaxScaler

data_frame = pd.read_csv("C:/Users/Admin/Desktop/breast cancer wisconsin dataset/breast-cancer-wisconsin.data")
# print(data_frame)
# remove noise or unknown values from dataset
data_frame.replace('?',1, inplace=True)


# dropping the first column which is id of the patient
data_frame.drop(['1000025'], 1, inplace=True)
# assigning all the attributes to x as numpy array
x = np.array(data_frame.drop(['2.1'], 1))
print(x)
# assigning output class to y as numpy array
y = np.array(data_frame['2.1'])
print(y)
scaler = MinMaxScaler()
x_scaled=scaler.fit_transform(x)
print(x_scaled)
db = DBSCAN(eps=1, min_samples=10).fit(x_scaled)
print(db.labels_)
print(sm.accuracy_score(y,db.labels_))
