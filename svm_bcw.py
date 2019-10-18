import numpy as np
from sklearn import preprocessing, neighbors, model_selection, svm
import pandas as pd

data_frame = pd.read_csv("C:/Users/Admin/Desktop/breast cancer wisconsin dataset/breast-cancer-wisconsin.data")

# remove noise or unknown values from dataset
data_frame.replace('?', -99999, inplace=True)

# dropping the first column which is id of the patient
data_frame.drop(['1000025'], 1, inplace=True)
# assigning all the attributes to x as numpy array
x = np.array(data_frame.drop(['2.1'], 1))
print(x)
# assigning output class to y as numpy array
y = np.array(data_frame['2.1'])
print(y)

# splitting training and test cases
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

# creating svm classifier
classifier = svm.SVC()

# training the model
classifier.fit(x_train, y_train)

# confidence score for the test cases
confidence = classifier.score(x_test, y_test)
print(confidence)

# creating new test example
new_test_example = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1]])
new_test_example = new_test_example.reshape(len(new_test_example), -1)
print(new_test_example)
# predicting op for new test case
prediction_result = classifier.predict(new_test_example)
if prediction_result == 2:
    print("Final class = {0}->{1}".format(prediction_result,"benign"))
else:
    print("Final class = {0}->{1}".format(prediction_result, "malignant"))

