import numpy as np
from numpy import genfromtxt
from decimal import *

getcontext().prec=3


data = genfromtxt("mumbai_data.csv",delimiter=',', names=True)

lis = ["Tests", "Infected", "Recovered", "Deceased"]
r = ["Mean", "Std. Dev."]

new_data=[]
new_data.append(["%0.3f"%(np.mean(data['Tests'],axis=0)),"%0.3f"%(np.std(data['Tests'],axis=0))])
new_data.append(["%0.3f"%(np.mean(data['Infected'],axis=0)),"%0.3f"%(np.std(data['Infected'],axis=0))])
new_data.append(["%0.3f"%(np.mean(data['Recovered'],axis=0)),"%0.3f"%(np.std(data['Recovered'],axis=0))])
new_data.append(["%0.3f"%(np.mean(data['Deceased'],axis=0)),"%0.3f"%(np.std(data['Deceased'],axis=0))])



row_format ="{:<15}" * (len(r)+1)
print(row_format.format("Field", *r))
for li, row in zip(lis, new_data):
    print(row_format.format(li, *row))


