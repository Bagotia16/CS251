from ring import *
import argparse

def S_3(k,x,n):
	sm = RingInt(n, 0)
	p = RingInt(n,x)
	for i in range(int(k)):
		j = RingInt(n, i+1)
		sm += j**p
	return sm

def S_1(k,x,n):
	sm=RingInt(n, 0)
	m=RingInt(n,1)
	x = RingInt(n,x)
	for i in range(int(k)):
		j = RingInt(n,i)
		t = (x**j)
		sm = sm + t/m
		k = RingInt(n,i+1)
		m = m*(k)
	return sm

def fac(x):
	f = 1
	for i in range(x):
		f = f*(i+1)
	return f

def comb(x,m,n):
	nm = RingInt(n, fac(x))
	dm = RingInt(n, fac(m)*fac(x-m))
	return nm/dm

def S_2(k,x,n):
	_k = 0
	t = RingInt(n, 0)
	while _k < k:
		_t = RingInt(n,0)
		for i in range(_k+1):
			_t += comb(x+_k,i,n)
		if _k >0:
			t = (aftr * _t)
		else:
			t.value = _t.value
		
		aftr = RingInt(n, t.value)

		_k += 1

	return aftr


def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-inp', required=True)
	parser.add_argument('-out', required=True)
	args = parser.parse_args()
	f1 = open(args.inp, "r")
	file = open(args.out, "w")
	# lines=f1.readlines()
	# lines=lines[:-1]
	for line in f1:
		L = line.split(" ")
		L[-1]=L[-1].strip()
		k,x,n,S = int(L[0]),int(L[1]),int(L[2]),int(L[3])
		if S==1:
			try:
				ans  = (S_1(k,x,n))
				file.write(str(ans))
			except:
				file.write("UNDEFINED")
		elif S==2:
			try:
				ans = (S_2(k,x,n))
				file.write(str(ans))
			except:
				file.write("UNDEFINED")
		elif S==3:
			try:
				ans = S_3(k,x,n)
				file.write(str(ans))
			except:
				file.write("UNDEFINED")
		file.write("\n")
	file.close()
	f1.close()



if __name__=="__main__":
	main()