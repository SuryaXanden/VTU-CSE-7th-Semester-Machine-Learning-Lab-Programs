import pandas as pd
dataset = pd.read_csv('1.csv').values
data = []
for row in dataset:
    if row[-1].upper()=="YES":
        data.append(row)
print("Positive examples are:")
for x in data:
    print(x)
print("\nSteps of FIND.S algorithm\n['%','%','%','%','%','%']")
hypo = data[0][:-1]
for i in range(len(data)):
    for j in range(len(data[0][:-1])):
        hypo[j] = '?' if hypo[j] != data[i][j] else hypo[j]
    print(hypo)
print("\nFIND.S algorithm output")
print(hypo)