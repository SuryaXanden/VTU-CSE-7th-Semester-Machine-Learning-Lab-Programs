import csv
import math
import random
def majorclass(at,d,t):   
    freq={}
    index = at.index(t)
    for tuple in d:
        if tuple[index] in freq:
            freq[tuple[index]]+=1
        else:
            freq[tuple[index]]=1
    max=0
    major=""
    for key in freq.keys():
        if freq[key]>max:
            max=freq[key]
            major=key
    return major
def entropy(at,d,tat):
    freq={}
    dE=0.0
    i=0
    for entry in at:
        if(tat==entry):
            break
        i=i+1
    i=i-1
    for entry in d:
        if entry[i] in freq:
            freq[entry[i]]+=1.0
        else:
            freq[entry[i]]=1.0
    for freq in freq.values():
        dE+=(-freq/len(d))*math.log(freq/len(d),2)
    return dE
def info_gain(at,d,attr,tat):
    freq={}
    ssE=0.0
    i=at.index(attr)
    for entry in d:
        if entry[i] in freq:
            freq[entry[i]]+=1.0
        else:
            freq[entry[i]]=1.0
    for entry in d:
        if entry[i] in freq:
            freq[entry[i]]+=1.0
        else:
            freq[entry[i]]=1.0
    for val in freq.keys():
        valprob=freq[val]/sum(freq.values())
        dss=[entry for entry in d if entry[i]==val]
        ssE+=valprob*entropy(at,dss,tat)
    return(entropy(at,d,tat)-ssE)
def attr_choose(d,at,t):
    best=at[0]
    maxGain=0
    for attr in at:
        newGain=info_gain(at,d,attr,t)
        if newGain>maxGain:
            maxGain=newGain
            best=attr
    return best
def get_values(d,at,attr):
    index=at.index(attr)
    values=[]
    for entry in d:
        if(entry[index] not in values):
            values.append(entry[index])
    return values
def get_data(d,at,best,val):
    new_data=[[]]
    index=at.index(best)
    for entry in d:
        if(entry[index]==val):
            newEntry=[]
            for i in range(0,len(entry)):
                if(i != index):
                    newEntry.append(entry[i])
                new_data.append(newEntry)
    new_data.remove([])
    return new_data
def build_tree(d,at,t):
    d=d[:]
    vals=[record[at.index(t)]for record in d]
    default=majorclass(at,d,t)
    if not d or (len(at)-1)<=0:
        return default
    elif vals.count(vals[0])==len(vals):
        return vals[0]
    else:
        best =  attr_choose(d,at,t)
        tree={best:{}}
        for val in get_values(d,at,best):
            new_data=get_data(d,at,best,val)
            newAttr=at[:]
            newAttr.remove(best)
            subtree=build_tree(new_data,newAttr,t)
            tree[best][val]=subtree
    return tree
def execute_decision_tree():
    d=[]
    with open("3.csv") as tsv:
        for line in csv.reader(tsv):
            d.append(tuple(line))
        print("no of records ",len(d))
        at=['outlook','temperature','humidity','wind','play']
        t=at[-1]
        acc=[]
        training_set=[x for i,x in enumerate(d)]
        tree=build_tree(training_set,at,t)
        print(tree)
        result=[]
        test_set=[('rainy','mild','high','strong')]
        for entry in test_set:
                tempDict=tree.copy()
                result=""
                while(isinstance(tempDict, dict)):
                    child=[]
                    nodeVal=next(iter(tempDict))
                    child=tempDict[next(iter(tempDict))].keys()
                    tempDict=tempDict[next(iter(tempDict))]
                    index=at.index(nodeVal)
                    value=entry[index]
                    if value in tempDict.keys():
                        result=tempDict[values]
                        tempDict=tempDict[values]
                    else:
                        result="NULL"
                        break
                if result!="NULL":
                    result.append(result==entry[-1])
    print(result)
execute_decision_tree()