import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import math
# plt.style.use('dark_background')


url = "https://api.covid19india.org/csv/latest/case_time_series.csv"

# x = requests.get("https://api.covid19india.org/csv/latest/case_time_series.csv")
# data = x.content

df = pd.read_csv(url) 
_df = df.iloc[76:]

arr = _df["Total Deceased"].to_numpy()

H = np.zeros(len(arr))
H[0] = arr[0]/df.loc[75, 'Total Deceased']
for i in range(1, len(arr)):
    H[i] = arr[i]/arr[i-1]

l = np.arange(1, len(H)+1, 1).tolist()
l = np.array(l)

plt.scatter(l, H, color="r")

H1 = np.empty(len(H)+1)
H1.fill(1)


m,b = np.polyfit(l,H,1)
# print(m,b)
end_point_x = (1-b)/m 
print(math.ceil(end_point_x))

line = [ (m*i)+b for i in l ]

l = np.append(l, end_point_x)
line = np.append(line, 1)

plt.plot(l, line, color="k")
plt.plot(l, H1, color="c")

plt.xlabel("number of days starting from 15 April")
plt.ylabel("H(t)")
plt.title("Death rate of Covid19 in India")
plt.legend(["best fit line", "Y=1 line", "H(t) plot"], loc="upper right")
# plt.show()
plt.savefig("covid.png")