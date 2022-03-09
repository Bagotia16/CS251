def rotate(m):
	n=len(m[0])
	for i in range(n//2):
		for j in range(i,n-i-1):
			var=m[i][j]
			m[i][j]=m[n-1-j][i]
			m[n-j-1][i]=m[n-i-1][n-j-1]
			m[n-i-1][n-j-1]=m[j][n-i-1]
			m[j][n-i-1]=var

	return m

s = input()
l=[]
l.append(s.split(" "))

n=len(l[0])
for x in range(n-1):
	s=input()
	l.append(s.split(" "))

m=rotate(l)
for x in range(n):
	for y in range(n):
		if y!=(n-1):
			print(m[x][y],end=" ")
		else:
			print(m[x][y],end="")
	print()


