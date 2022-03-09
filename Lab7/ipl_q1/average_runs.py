import sqlite3
conn=sqlite3.connect('ipl.db')

cursor= conn.execute('''select venue_name,z from 
						(select match.match_id,venue_name,avg(x) as z from 
						match,(select match_id,sum(runs_scored)+sum(extra_runs) as x 
						from BALL_BY_BALL group by match_id) as y 
						where match.match_id=y.match_id 
						group by venue_name 
						order by z DESC);''')

for row in cursor:
	for cell in row[:-1]:
		print(cell, end=",")
	print(row[-1])