from math import exp
from random import random
from random import seed
def initialize_nw(ip, hid, op):
    nw = list()
    hl = [{'wt':[random() for i in range(ip + 1)]} for i in range(hid)]
    nw.append(hl)
    ol = [{'wt':[random() for i in range(hid + 1)]} for i in range(op)]
    nw.append(ol)
    return nw
def activate(wt, inputs):
    act = wt[-1]
    for i in range(len(wt)-1):
        act += wt[i] * inputs[i]
    return act
def transfer(act):
    return 1.0 / (1.0 + exp(-act))
def forward_propagate(nw, row):
    inputs = row
    for l in nw:
        new_inputs = []
        for neuron in l:
            act = activate(neuron['wt'], inputs)
            neuron['op'] = transfer(act)
            new_inputs.append(neuron['op'])
        inputs = new_inputs
    return inputs    
def transfer_derivative(output):
    return output * (1.0 - output)
def bpe(nw, expected):
    for i in reversed(range(len(nw))):
        l = nw[i]
        errors = list()
        if i != len(nw)-1:
            for j in range(len(l)):
                error = 0.0
                for neuron in nw[i+1]:
                    error += (neuron['wt'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(l)):
                neuron = l[j]
                errors.append(expected[j] - neuron['op'])
        for j in range(len(l)):
            neuron = l[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['op'])                
def update_wt(nw, row, l_rate):
    for i in range(len(nw)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['op'] for neuron in nw[i -1]]
        for neuron in nw[i]:
            for j in range(len(inputs)):
                neuron['wt'][j] += l_rate * neuron['delta'] * inputs[j]
            neuron['wt'][-1] += l_rate * neuron['delta']
def train_nw(nw, train, l_rate, n_epoch, op):
    for epoch in range(n_epoch):
        sume = 0
        for row in train:
            outputs = forward_propagate(nw, row)
            expected = [0 for i in range(op)]
            expected[row[-1]] = 1
            sume += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(expected))])
            bpe(nw, expected)
            update_wt(nw, row, l_rate)
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sume))
seed(1)
dataset = [[2.78,2.55, 0], [1.46, 2.36, 0],[3.39, 4.40, 0],[1.38, 1.85, 0],[3.06, 3.00, 0],[7.62, 2.75, 1],[5.33, 2.08, 1],[6.92, 1.77, 1],[8.67, -0.24, 1],[7.67, 3.50,1]]
ip = len(dataset[0]) - 1
op = len(set([row[-1] for row in dataset]))
nw = initialize_nw(ip, 2, op)
print(nw)
train_nw(nw, dataset, 0.5, 20, op)
for l in nw:
    print(l)
