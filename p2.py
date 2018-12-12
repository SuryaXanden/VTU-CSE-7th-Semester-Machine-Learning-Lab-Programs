import numpy as np
import pandas as pd
data = pd.read_csv('2.csv')
con = np.array(data.iloc[:,:-1]) # without yes/no
tar = np.array(data.iloc[:,-1]) # YES/NO
def learn(con,tar):
    sh = con[0]
    print("Initialization of specific hypothesis and general hypothesis")
    print(sh)
    gh = [["?" for i in range(len(sh))] for i in range(len(sh))]
    print(gh)
    for i,h in enumerate(con):
        if tar[i] == "YES":
            for x in range(len(sh)):
                if h[x] != sh[x]:
                    gh[x][x] = sh[x] = '?'
        if tar[i] == "NO":
            for x in range(len(sh)):
                if h[x] != sh[x]:
                    gh[x][x] = sh[x]
        else:
            gh[x][x] = '?'
        print("steps of candidate eliminate algorithm",i+1)
        print(sh)
        print(gh)
    indices=[i for i,val in enumerate(gh) if val == ['?','?','?','?','?','?']]
    for i in indices:
        gh.remove(['?','?','?','?','?','?'])
    return sh,gh
s,g = learn(con,tar)
print("Final sh",s)
print("Final gh",g)