from ring import *

class Series:

	def __init__(self,k,x,n):
		self.k = int(k)
		self.value = int(x)
		self.n = int(n)

	def __iter__(self):
		self.i = 0
		return self

	def fac(self, x):
		f = 1
		for i in range(x):
			f = f*(i+1)
		return f

	def __next__(self):
		if self.i < self.k:
			m = RingInt(self.n, self.fac(self.i))
			x = RingInt(self.n, self.value)
			j = RingInt(self.n, self.i)
			_p = (x**j)
			trm = _p/m
			self.i+=1
			return trm
		else:
			raise StopIteration


def main():

	in_str = str(input())
	in_list = in_str.split(' ')
	k, x, n = in_list[0], in_list[1], in_list[2]
	for ele in Series(k, x, n):
			print(ele)


if __name__=="__main__":
	main()
