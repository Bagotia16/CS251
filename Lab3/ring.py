class RingInt:
	def __init__(self, characteristic, value):
		self.characteristic = characteristic
		self.value = value

	def __str__(self):
		return str(self.value) + '[' + str(self.characteristic) + ']'

	def __add__(self, b):
		return  RingInt(self.characteristic, int((self.value + b.value)%self.characteristic))

	def __sub__(self, b):
		if a - b < 0:
			return RingInt(self.characteristic, (self.characteristic + self.value-b.value)%self.characteristic)
		else:
			return RingInt(self.characteristic, (self.value-b.value)%self.characteristic)

	def __mul__(self, b):
		return RingInt(self.characteristic, (self.value*b.value)%self.characteristic)

	def gcd(self,a,b):
		if(b==0):
			return a
		else:
			return self.gcd(b, a%b)

	def __truediv__(self, b):
		if self.characteristic != b.characteristic or b.value == 0:
			raise ValueError("UNDEFINED")
		else:
			for i in range(b.characteristic):
				if (b.value*i)%self.characteristic == self.value:
					if self.gcd(i, self.characteristic) == 1:
						return RingInt(self.characteristic, i)
					else: 
						pass
				else:
					pass
			raise ValueError("UNDEFINED")



	def __pow__(self, b):
		return RingInt(self.characteristic, (self.value**b.value)%self.characteristic)

	def __eq__(self, b):
		if self.characteristic == b.characteristic and self.value == b.value:
			return True
		else:
			return False