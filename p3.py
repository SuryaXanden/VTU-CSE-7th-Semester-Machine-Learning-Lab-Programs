import pandas as pd
import math
import random
import numpy as np
def Mjclass(at,data,T):
    f = {}
    index = at.index(T)
    for el in data:
        f[el[index]] = f[el[index]]+1 if el[index] in f else 1
    max = 0
    for key in f.keys():
        if f[key] > max:
            max = f[key]
    return max

def entropy(at,data,tat):
    f = {}
    i = 0
    for e in at:
        if tat == e:
            break
        i += 1
    i -= 1
    dE = 0
    for e in data:
        f[e[i]] = f[e[i]]+1 if e[i] in f else 1
    for f in f.values():
        dE += (-f/len(data))*math.log(f/len(data),2)
    return dE

def info_gain(at,data,attr,tat):
    f = {}
    i = at.index(attr)
    for e in data:
        f[e[i]] = f[e[i]]+1 if e[i] in f else 1
    ssE = 0
    for k in f.keys():
        valProb = f[k] / sum(f.values())
        datasubset = [e for e in data if e[i] == k]
        ssE += valProb * entropy(at,datasubset,tat)
    return(entropy(at,data,tat)-ssE)

def attr_choose(data,at,T):
    best = at[0]
    G = 0
    for attr in at:
        g = info_gain(at,data,attr,T)
        if g > G:
            G = g
            best = attr
    return best

def get_values(data,at,attr):
    i=at.index(attr)
    v=[]
    for e in data:
        if e[i] not in v:
            v.append(e[i])
    return v

def get_data(data,at,best,val):
    D = [[]]
    index = at.index(best)
    for e in data:
        if e[index] == val:
            E = []
            for i in range(len(e)):
                if i != index:
                    E.append(e[i])
            D.append(E)
    D.remove([])
    return D

def build_tree(data,at,T):
    vals = [e[at.index(T)] for e in data]
    if not data or len(at)-1 <= 0:
        return Mjclass(at,data,T)
    elif vals.count(vals[0]) == len(vals):
        return vals[0]
    else:
        best = attr_choose(data,at,T)
        tree = {best:{}}
        for val in get_values(data,at,best):
            new_data = get_data(data,at,best,val)
            newAttr = at[:]
            newAttr.remove(best)
            tree[best][val] = build_tree(new_data,newAttr,T)
    return tree
    
def execute_decision_tree():
    data = pd.read_csv('3.csv').values
    print("Number of records:",len(data))
    at = ['outlook','temperature','humidity','wind','play']
    T = at[-1]
    train = [np.array(i) for i in data]
    tree = build_tree(train,at,T)
    # print(tree)
    test = [('sunny','hot','high','week')]
    for e in test:
        tmp = tree.copy()
        result = ''
        while isinstance(tmp, dict):
            nodeVal = next(iter(tmp))
            tmp = tmp[next(iter(tmp))]
            index = at.index(nodeVal)
            value = e[index]
            if value in tmp.keys():
                result = tmp[value]
                tmp = tmp[value]
            else:
                result = "Null"
                break
    print(result)
execute_decision_tree()