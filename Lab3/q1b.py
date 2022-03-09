import argparse

def decode_msg(file_name):

	with open(file_name) as f:
		first_line=f.readline()

	n = int(first_line)
	file = open(file_name, "r")

	msg = []
	for line in file:
		for word in line.split():
			if word.startswith('$') and word.endswith('$') or word.startswith('$') and word.endswith('.'):
				if '#' not in word:
					continue;
				else:
					temp = word
					temp = temp.replace('$','')
					temp = temp.replace('(','')
					temp = temp.replace(')','')
					temp = temp.replace('#','')
					temp = temp.replace(',','')
					temp = temp.replace('.','')
					if temp.isdigit():
						msg.append(word)
						# print(word)
					else:
						pass

	a_b = True
	b_b = True
	for i in range(len(msg)):	
		temp = msg[i].replace('$','')
		temp = temp.replace('(','')
		temp = temp.replace(')','')
		temp = temp.replace('.','')
		b = True
		a_i = 1
		b_i = 1
		sum_a = 0
		sum_b = 0
		for j in temp:
			if j == '#':
				b = False

			if b == True:
				if j != ',':
					if int(j) >= n:
						a_b = False
					else:
						sum_a += int(j)*a_i
						a_i += 1

			elif b == False:
				if j != ',' and j != '#':
					if int(j) >= n:
						b_b = False
					else:
						sum_b += int(j)*b_i
						b_i += 1

		if sum_a%n != 0:
			a_b = False
		if sum_b%n != 0:
			b_b = False


	if a_b == False or b_b == False:
		print("CORRUPTED")
	else:
		print("OK")


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-m', required=True)
	args = parser.parse_args()
	file_name = args.m
	with open(file_name) as f:
		first_line=f.readline()
	decode_msg(args.m)

if __name__=="__main__":
	main()