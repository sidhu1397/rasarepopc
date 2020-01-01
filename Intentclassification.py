import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
import nltk
import re
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Bidirectional, Embedding, Dropout, Flatten, GlobalAveragePooling1D,GRU
from keras.callbacks import ModelCheckpoint
from nltk.corpus import stopwords
import pickle
from nltk.stem import WordNetLemmatizer

# nltk.download('wordnet')



def load_dataset(filename):
    df = pd.read_excel(filename, encoding="latin1")
    print(df.head())
    intent = df["Intent"]
    unique_intent = list(set(intent))
    sentences = list(df["Clean Description"])
    df.dropna(axis=0, how='any')

    return (intent, unique_intent, sentences)


intent, unique_intent, sentences = load_dataset("C:\\Users\\Admin\\Desktop\\GFile_243.xlsx")
# print(type(intent))
# print(sentences)
# print(type(sentences))
# nltk.download("stopwords")
# nltk.download("punkt")
#
#
#
lemmatizer = WordNetLemmatizer()

stop_words = (set(stopwords.words('english')))
words = []

#
# def cleaning(sentences):
#     for s in sentences:
#         clean = re.sub(r'[^ a-z A-Z 0-9]', " ", str(s))
#         w = word_tokenize(clean)
#         # print(type(w))
#         # stemming
#         words.append([lemmatizer.lemmatize(i.lower()) for i in w if (i not in stop_words and len(i) > 1)])
#         # words.append([stemmer.stem(i.lower()) for i in w])
#
#     return words
#
#
# cleaned_words = cleaning(sentences)
# print(len(cleaned_words))
# print(cleaned_words)
#
#
# def create_tokenizer(words, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'):
#     token = Tokenizer(filters=filters)
#     token.fit_on_texts(words)
#     return token
#
#
# def max_length(words):
#     return (len(max(words, key=len)))
#
#
# word_tokenizer = create_tokenizer(cleaned_words)
# vocab_size = len(word_tokenizer.word_index) + 1
# max_length = max_length(cleaned_words)
#
# import pickle
#
# # saving
# with open('tokenizer.pickle', 'wb') as handle:
#     pickle.dump(word_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
#
#
# print("Vocab Size = %d and Maximum length = %d" % (vocab_size, max_length))
#
#
# def encoding_doc(token, words):
#     return (token.texts_to_sequences(words))


# encoded_doc = encoding_doc(word_tokenizer, cleaned_words)


def padding_doc(encoded_doc, max_length):
    return (pad_sequences(encoded_doc, maxlen=max_length, padding="post"))


# padded_doc = padding_doc(encoded_doc, max_length)
#
# print("Shape of padded docs = ", padded_doc.shape)
#
# # tokenizer with filter changed
# output_tokenizer = create_tokenizer(unique_intent, filters='!"#$%&()*+,-/:;<=>?@[\]^`{|}~')
#
# encoded_output = encoding_doc(output_tokenizer, intent)
#
# encoded_output = np.array(encoded_output).reshape(len(encoded_output), 1)
#
# print("output class shape {0}".format(encoded_output.shape))
#
#
# def one_hot(encode):
#     o = OneHotEncoder(sparse=False)
#     return (o.fit_transform(encode))
#
#
# output_one_hot = one_hot(encoded_output)
# from sklearn.model_selection import train_test_split
#
# train_X, val_X, train_Y, val_Y = train_test_split(padded_doc, output_one_hot, shuffle=True, test_size=0.20)
# print("Shape of train_X = %s and train_Y = %s" % (train_X.shape, train_Y.shape))
# print("Shape of val_X = %s and val_Y = %s" % (val_X.shape, val_Y.shape))
#
#
# def create_model(vocab_size, max_length):
#     model = Sequential()
#     model.add(Embedding(vocab_size, 128, input_length=max_length, trainable=False))
#     # model.add(GlobalAveragePooling1D())
#     model.add(Bidirectional(GRU(128)))
#     # model.add(LSTM(128))
#     # model.add(Flatten())
#     model.add(Dense(20, activation="relu"))
#     model.add(Dropout(0.5))
#     model.add(Dense(7, activation="softmax"))
#
#     return model
#
#
# model = create_model(vocab_size, max_length)
#
# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# model.summary()
#
# filename = 'model_new.h5'
# # checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
#
# model.fit(padded_doc, output_one_hot, epochs=50, batch_size=32, validation_data=(val_X, val_Y))
# # , validation_data = (val_X, val_Y),callbacks=[checkpoint]
# model.save("model_new.h5")
model1 = load_model("model_new.h5")

# loss, accuracy = model.evaluate(padded_doc, output_one_hot)
# print("Validation loss ={0}".format(loss))
# print("Validation Accuracy = {0}".format(accuracy))


def predictions(text):
    clean = re.sub(r'[^ a-z A-Z 0-9]', " ", text)
    test_word = word_tokenize(clean)
    test_word = [lemmatizer.lemmatize(w.lower()) for w in test_word if (w not in stop_words and len(w) > 1)]
    # loading tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        word_tokenizer = pickle.load(handle)
    test_ls = word_tokenizer.texts_to_sequences(test_word)
    print(test_word)
    # Check for unknown words
    if [] in test_ls:
        test_ls = list(filter(None, test_ls))

    test_ls = np.array(test_ls).reshape(1, len(test_ls))

    x = padding_doc(test_ls, 20)

    pred = model1.predict_proba(x)

    return pred


def get_final_output(pred, classes):
    predictions = pred[0]

    classes = np.array(classes)
    ids = np.argsort(-predictions)
    classes = classes[ids]
    predictions = -np.sort(-predictions)

    for i in range(pred.shape[1]):
        print("%s has confidence = %s" % (classes[i], (predictions[i])))


print(unique_intent)
text = "Please Install Gfile on this machine"
pred = predictions(text)
print(pred)
get_final_output(pred, unique_intent)
