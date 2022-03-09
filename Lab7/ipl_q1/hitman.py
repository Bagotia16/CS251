import sqlite3
conn=sqlite3.connect('ipl.db')

cursor=conn.execute("select player_id,player_name,x,y,z from player,(select striker,x,y,x*1.0/y as z from (select striker,count(runs_scored) as y,sum(case when runs_scored=6 Then 1 else 0 end) as x from BALL_BY_BALL group by striker)) where player_id=striker order by z DESC, player_name ASC;")

for row in cursor:
	for cell in row[:-1]:
		print(cell, end=",")
	print(row[-1])