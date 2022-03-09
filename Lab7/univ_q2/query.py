import sqlite3
import sys


conn = sqlite3.connect('univ.db')

table = sys.argv[2]
colum = sys.argv[3]
value = sys.argv[4]

# print(sys.argv[1])

if sys.argv[1]=="0":
	# print(table)
	# print(value)
	statement="SELECT * FROM "+table+" WHERE "+colum+" = '"+value+"';"
	# for query in statement.split(";"):
	try: 
		cursor = conn.execute(statement)
		for row in cursor:
			for cell in row[:-1]:
				print(cell, end=",")
			print(row[-1])
	except:pass

if sys.argv[1]=="1":
	# print(colum)
	# print(value)
	# statement="SELECT * FROM "+table+" WHERE "+colum+" = @0"
	cursor = conn.execute("SELECT * FROM " +table+ " where "+colum+" =?",(value,))
	# cursor.execute("SELECT * FROM classroom where building=%s'", (value, ));
	# conn.commit()
	for row in cursor:
		for cell in row[:-1]:
			print(cell, end=",")
		print(row[-1])
		# print(row)



