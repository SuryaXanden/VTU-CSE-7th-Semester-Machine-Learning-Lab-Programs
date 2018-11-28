import csv
hypo = ['%','%','%','%','%','%']
with open ('1.csv') as csv_file:
    reader = csv.reader(csv_file)
    data = []
    for row in reader:
        if row[len(row)-1].upper() == "YES":
            data.append(row)
print('The Training Examples are :\n')
for x in data:
    print(x)
print('\n')
i=j=k=p=0
print('Steps of find-S Algorithm :\n')
list = [] 
for j in range(len(data[p])):
    list.append(data[i][j])
hypo = list
for i in range(1,len(data)):
	for k in range(len(data[p])):
		if hypo[k] != data[i][k]:
			hypo[k] = '?'
			k += 1
	print(hypo)
i += 1
print('\nMax Specific Find-S hypothesis for given csv are :\n')
list = []
for i in range(len(data[p])):
    list.append(hypo[i])
print(list)