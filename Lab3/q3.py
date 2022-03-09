from collections import Counter 
import argparse
from argparse import ArgumentParser

parser = ArgumentParser(description="max money earned")
parser.add_argument("-ca", dest="candies", required=True,
    help="input file with type of candies", metavar="FILE")
parser.add_argument("-ch", dest="children", required=True,
    help="input file with children desires", metavar="FILE")
args = parser.parse_args()


# parser = ArgumentParser(description="max money earned")
# parser.add_argument("-ch", dest="children", required=True,
#     help="input file with children desires", metavar="FILE")
# args = parser.parse_args()

def myfunc(e):
	return int(e[1])

f1=open(args.candies,"r")
n1=f1.readline()
l1=f1.readline().split(" ")
l1[-1] = l1[-1].strip()
cnt=Counter(l1)
# print(l1)

f2=open(args.children,"r")
n2=f2.readline()
l2=[]
for x in range(int(n2)):
	l2.append(f2.readline().split(" "))


l2.sort(reverse=True, key=myfunc)
# print l2

sum=0
for i in range(int(n2)):
	if cnt[l2[i][0]] > 0:
		sum=sum+int(l2[i][1])
		# print sum
		# print l1
		#l1.remove(l2[i][0])
		cnt[l2[i][0]]-=1

print(sum)
f2.close()
