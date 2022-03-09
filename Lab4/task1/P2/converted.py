import numpy as np
from numpy import genfromtxt
import csv

lis = ["Day", "Tests per Million", "Test Positivity rate", "Recovered", "Deceased"]

with open("transformed.csv", "w") as file:
	f2 = csv.writer(file)
	with open("mumbai_data.csv", "r") as csvfile:
		data=csv.reader(csvfile, delimiter=',')
		line_cnt=0
		# row_format ="{:<15}" * (len(lis)+1)
		for row in data:
			if line_cnt == 0:
				f2.writerow([*lis])
				line_cnt+=1
			else:
				row[2]="%0.3f"%(int(row[2])/int(row[1]))
				row[1]=int(int(row[1])/20.4)
				f2.writerow([*row])
				line_cnt+=1

file.close()
csvfile.close()