import numpy as np
import csv

lis = ["Day", "Infected(Unlock)", "Infected(Lock)", "Positivity Rate(Lock)", "Positivity Rate(Unlock)"]

reader1 = open("mumbai_data.csv","r")
# reader1.readline()
data1 = csv.reader(reader1,delimiter=',')
reader2 = open("mumbai_unlock.csv","r")
# reader2.readline()
data2 = csv.reader(reader2, delimiter=',')
file = open("info_combine.csv", "w")
f = csv.writer(file)
line_cnt=0
for (row1,row2) in zip(data1,data2):
	if line_cnt == 0:
		f.writerow([*lis])
		line_cnt+=1
	else:
		row1[3]="%0.3f"%(int(row1[2])/int(row1[1]))
		row2[3]="%0.3f"%(int(row2[2])/int(row2[1]))
		f.writerow([row1[0],row2[2],row1[2],row1[3],row2[3]])
		line_cnt+=1

file.close()