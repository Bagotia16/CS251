import sqlite3
cnn = sqlite3.connect('ipl.db')

cur = cnn.execute('''select player_id, player_name, x from
                    (select player.player_id, player.player_name, count(out_type) as x
                    from PLAYER, BALL_BY_BALL as y
                    where player.player_id=y.bowler and out_type != 'Not Applicable'
                    group by player_id
                    )
                    order by x DESC,player_name
                    ''')

i=0
for row in cur:
    if i<20:
        for cell in row[:-1]:
            print(cell, end=",")
        i+=1
        print(row[-1])
