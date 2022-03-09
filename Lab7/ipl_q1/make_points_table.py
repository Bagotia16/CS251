import sqlite3

sql_points_table = '''CREATE TABLE POINTS_TABLE(
                      team_id         int,
                      team_name       text,
                      points          int,
                      nrr             int
)'''

sql_win = '''SELECT team1, team2, match_winner, win_type, win_margin
             FROM MATCH
'''

sql_team = '''SELECT team_id, team_name
              FROM TEAM
'''

cnn = sqlite3.connect('ipl.db')
cursor = cnn.cursor()

cursor.execute(sql_points_table)

#match_winner, win_type, win_margin

team_values = cnn.execute(sql_team)
win_details = cnn.execute(sql_win)

l=[]
for row in team_values:
    for cell in row:
        l.append(cell)

win_detail = []
for row in win_details:
    for cell in row:
        win_detail.append(cell)

points=[]
nrr=[]
for i in range(int(len(l)/2)):
    points.append(0)
    nrr.append(0)

for i in range(1, int(len(win_detail)/5.0)+1):
    if win_detail[5*i-2] == 'runs':
        points[int(win_detail[5*i-3])-1] += 2
        t = win_detail[5*i-1]/20
        if win_detail[5*i-5] == win_detail[5*i-3]:
            nrr[int(win_detail[5*i-3])-1] += t 
            nrr[int(win_detail[5*i-4])-1] -= t
        else:
            nrr[int(win_detail[5*i-3])-1] += t
            nrr[int(win_detail[5*i-5])-1] -= t
            
    elif win_detail[5*i-2] == 'wickets':
        points[int(win_detail[5*i-3])-1] += 2
        t = win_detail[5*i-1]/10
        if win_detail[5*i-5] == win_detail[5*i-3]:
            nrr[int(win_detail[5*i-3])-1] += t 
            nrr[int(win_detail[5*i-4])-1] -= t
        else:
            nrr[int(win_detail[5*i-3])-1] += t
            nrr[int(win_detail[5*i-5])-1] -= t

    elif win_detail[5*i-2] == 'Tie':
        points[int(win_detail[5*i-5])-1] += 1
        points[int(win_detail[5*i-4])-1] += 1

    else:
        points[int(win_detail[5*i-5])-1] += 1
        points[int(win_detail[5*i-4])-1] += 1

def valueToInsert(x):
    for i in range(1,x+1):
        yield l[2*i-2], l[2*i-1], points[i-1], nrr[i-1] 


cursor.executemany("""
                    INSERT INTO POINTS_TABLE ('team_id', 'team_name', 'points', 'nrr')
                    VALUES (?, ?, ?, ?)
        """, valueToInsert(int(len(l)/2)))

cnn.commit()

output = cursor.execute('''SELECT * FROM POINTS_TABLE
                           ORDER BY points DESC, nrr DESC''')

for row in output:
    for cell in row[:-1]:
        print(cell, end=",")
    print(row[-1])

cnn.close()
