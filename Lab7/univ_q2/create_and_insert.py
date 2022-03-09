import sqlite3
conn = sqlite3.connect('univ.db')
# print("Opened db Successfully")
f1 = open("University Schema","r")
f2 = open("smallRelationsInsertFile.sql","r")

sql = f1.read()
sql2 = f2.read()

for line in sql.split(';'):
	try: cursor1=conn.execute(line+";")
	except:pass
	
conn.executescript(sql2)

# cur = conn.execute("Select * from classroom")
# for row in cur:
# 	print(row)
