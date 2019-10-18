import numpy as np
from sklearn import preprocessing, neighbors, model_selection, svm
import pandas as pd

data_frame = pd.read_excel('C:/Users/Admin/Desktop/cars.xls')
# print(data_frame)

data_frame.replace('?', -99999, inplace=True)

x = np.array(data_frame.drop(['CYL'], 1))
print(x)
y = np.array(data_frame['CYL'])
print(y)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

classifier = svm.SVC()

classifier.fit(x_train, y_train)

confidence = classifier.score(x_test, y_test)
print(confidence)

new_test_example = np.array([[32.7, 168, 2910]])
new_test_example = new_test_example.reshape(len(new_test_example), -1)
print(new_test_example)
prediction_result = classifier.predict(new_test_example)
print("Output class = {0}".format(prediction_result))