import pandas as pd
import numpy as np
df = pd.read_csv('database.csv',low_memory=False)
name = df.SpeciesName.tolist()
damage = df.AircraftDamage.tolist()

uname=[]
udamage=[]

for i in range(len(name)):
    if name[i] in uname:
        continue
    else:
        uname.append(name[i])
        for j in range(i+1,len(name)):
            if name[i]==name[j]:
                damage[i]+=damage[j]
        udamage.append(damage[i])

maxi=max(udamage)
pos=udamage.index(maxi)
print("maximum is:",maxi," by ",uname[pos])
            
p=df.iloc[:, np.r_[38:51:2,53:65:2,65]]
a=p.sum(axis = 0, skipna = True)
maxi=max(a)
pos=a.idxmax(maxi)
print("Maximum damage(",maxi,"times) is done at",pos)              

