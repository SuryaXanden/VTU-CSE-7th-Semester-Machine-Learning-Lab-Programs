import numpy as np
from sklearn import metrics
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
categories = ['alt.atheism','soc.religion.christian','comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset = 'train',categories = categories,shuffle = True)
twenty_test = fetch_20newsgroups(subset = 'test',categories = categories,shuffle = True)
print('\n'.join(twenty_train.data[0].split("\n")))
count_vect = CountVectorizer()
trtf = CountVectorizer().fit_transform(twenty_train.data)
tff = TfidfTransformer()
train = tff.fit_transform(trtf)
mod = MultinomialNB()
mod.fit(train, twenty_train.target)
test = CountVectorizer().transform(twenty_test.data)
tf = tff.transform(test)
predicted = mod.predict(tf)
print("Accuracy: ", accuracy_score(twenty_test.target, predicted))
print(classification_report(twenty_test.target, predicted, target_names = twenty_test.target_names))
print("Confusion matrix is \n",metrics.confusion_matrix(twenty_test.target, predicted))