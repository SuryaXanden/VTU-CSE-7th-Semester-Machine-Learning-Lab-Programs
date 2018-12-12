import csv
import random
import math
import operator
def load(file, split, train, test):
    with open(file) as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                train.append(dataset[x])
            else:
                test.append(dataset[x])
def ed(i1, i2, length):
    d = 0
    for x in range(length):
        d += (i1[x] - i2[x])**2
    return d**.5
def get(train, test, k):
    dists = []
    for x in range(len(train)):
        dist = ed(test, train[x], len(test)-1)
        dists.append((train[x], dist))
    dists.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(dists[x][0])
    return neighbors
def response(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        classVotes[response] = classVotes[response] + 1 if response in classVotes else 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0] 
def accuracy(test, predict):
    correct = 0
    for x in range(len(test)):
        if test[x][-1] == predict[x]:
            correct += 1
    return (correct/float(len(test))) * 100
train=[]
test=[] 
split = 0.67
load('9.csv', split, train, test)
print ('Number of Training data: ', str(len(train)))
print ('Number of Test Data: ', str(len(test)))
predict=[]
k = 3
print('\nThe predict are: ')
for x in range(len(test)):
    neighbors = get(train, test[x], k)
    result = response(neighbors)
    predict.append(result)
    print('Predicted: ',str(result),'\Tactual: ',str(test[x][-1]))
print('\nThe Accuracy is: ', accuracy(test, predict))