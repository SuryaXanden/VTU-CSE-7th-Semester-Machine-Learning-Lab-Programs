from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn import metrics
import numpy as np
train = fetch_20newsgroups(subset = 'train')
print(train.target_names)
print("Length of the train:",len(train))
text = Pipeline([('vect',CountVectorizer()),('tfidf',TfidfTransformer()),('clf',MultinomialNB())])
text = text.fit(train.data,train.target)
test = fetch_20newsgroups(subset = 'test')
pd = text.predict(test.data)
acc = np.mean(test.target)
print("Prediction Accuracy =",acc)
print("Accuracy =",metrics.accuracy_score(test.target,pd))
print("Precision =",metrics.precision_score(test.target,pd,average = None))
print("Recall =",metrics.recall_score(test.target,pd,average = None))
print(metrics.classification_report(test.target,pd))