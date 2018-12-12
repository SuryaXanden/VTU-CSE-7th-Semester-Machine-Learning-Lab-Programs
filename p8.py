import numpy as np
import math
import matplotlib.pyplot as plt
import csv
def like(obs,probs):
    N = sum(obs)
    k = obs[0]
    bc = math.factorial(N) / (math.factorial(N-k) * math.factorial(k))
    prod_probs = obs[0] * math.log(probs[0]) + obs[1] * math.log(1-probs[0])
    return bc + prod_probs
with open("8.csv") as tsv:
    for line in csv.reader(tsv):
        data = [int(i) for i in line]
heads = np.array(data)
tails = 10-heads
sample = list(zip(heads,tails))
pA = np.zeros(100)
pA[0] = 0.60
pB = np.zeros(100)
pB[0] = 0.50
delta = 0.001
j=0
improvement = float('inf')
while(improvement > delta):
    eA = np.zeros((len(sample),2),dtype = float)
    eB = np.zeros((len(sample),2),dtype = float)
    for i in range(0,len(sample)):
        e=sample[i]
        ll_A = like(e,np.array([pA[j],1-pA[j]]))
        ll_B = like(e,np.array([pB[j],1-pB[j]]))
        wA = math.exp(ll_A)/(math.exp(ll_A)+math.exp(ll_B))
        wB = math.exp(ll_B)/(math.exp(ll_A)+math.exp(ll_B))
        eA[i] = np.dot(wA,e)
        eB[i] = np.dot(wB,e)
    pA[j+1] = sum(eA)[0]/sum(sum(eA))
    pB[j+1] = sum(eB)[0]/sum(sum(eB))
    improvement=(max(abs(np.array([pA[j+1],pB[j+1]])-np.array([pA[j],pB[j]]))))
    print(np.array([pA[j+1],pB[j+1]])-np.array([pA[j],pB[j]]))
    j+=1
plt.figure()
plt.plot(range(j),pA[:j])
plt.plot(range(j),pB[:j])
plt.show()