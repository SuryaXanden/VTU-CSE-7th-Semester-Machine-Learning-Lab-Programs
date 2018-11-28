import numpy as np
import math
import matplotlib.pyplot as plt
import csv
def likelihood(obs,probs):
    N = sum(obs)
    k = obs[0]
    binomial_coeff = math.factorial(N) / (math.factorial(N-k) * math.factorial(k))
    prod_probs = obs[0] * math.log(probs[0]) + obs[1] * math.log(1-probs[0])
    return (binomial_coeff + prod_probs)
data = []
with open("8.csv") as tsv:
    for line in csv.reader(tsv):
        data = [int(i) for i in line]
heads = np.array(data)
tails = 10-heads
sample = list(zip(heads,tails))
pA_heads = np.zeros(100)
pA_heads[0] = 0.60
pB_heads = np.zeros(100)
pB_heads[0] = 0.50
delta = 0.001
j=0
improvement = float('inf')
while(improvement > delta):
    exp_A = np.zeros((len(sample),2),dtype = float)
    exp_B = np.zeros((len(sample),2),dtype = float)
    for i in range(0,len(sample)):
        e=sample[i]
        ll_A = likelihood(e,np.array([pA_heads[j],1-pA_heads[j]]))
        ll_B = likelihood(e,np.array([pB_heads[j],1-pB_heads[j]]))
        weightA = math.exp(ll_A)/(math.exp(ll_A)+math.exp(ll_B))
        weightB = math.exp(ll_B)/(math.exp(ll_A)+math.exp(ll_B))
        exp_A[i] = np.dot(weightA,e)
        exp_B[i] = np.dot(weightB,e)
    0[j+1] = sum(exp_A)[0]/sum(sum(exp_A))
    pB_heads[j+1] = sum(exp_B)[0]/sum(sum(exp_B))
    improvement=(max(abs(np.array([pA_heads[j+1],pB_heads[j+1]])-np.array([pA_heads[j],pB_heads[j]]))))
    print(np.array([pA_heads[j+1],pB_heads[j+1]])-np.array([pA_heads[j],pB_heads[j]]))
    j+=1
plt.figure()
plt.plot(range(0,j),pA_heads[0:j])
plt.plot(range(0,j),pB_heads[0:j])
plt.show()