import sqlite3
import csv

cnn = sqlite3.connect('ipl.db')
cursor = cnn.cursor()

#teams
team = open("team.csv")
lines = csv.reader(team)
idx=0

for i in lines:
    if idx!=0:
        cursor.execute('''INSERT INTO TEAM 
                        VALUES (?,?)
        ''', i)
    idx+=1

#player_match
player_match = open("player_match.csv")
lines = csv.reader(player_match)
idx=0

for i in lines:
    if idx!=0:
        cursor.execute('''INSERT INTO PLAYER_MATCH
                          VALUES (?,?,?,?,?,?,?)
        ''', i)
    idx+=1

#player
player = open("player.csv")
lines = csv.reader(player)
idx=0

for i in lines:
    if idx!=0:
        cursor.execute('''INSERT INTO PLAYER
                          VALUES (?,?,?,?,?,?)
        ''', i)
    idx+=1

#match
match = open("match.csv")
lines = csv.reader(match)
idx=0

for i in lines:
    if idx!=0:
        cursor.execute('''INSERT INTO MATCH
                          VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        ''', i)
    idx+=1

#ball_by_ball
ball_by_ball = open("ball_by_ball.csv")
lines = csv.reader(ball_by_ball)
idx=0

for i in lines:
    if idx!=0:
        cursor.execute('''INSERT INTO BALL_BY_BALL
                          VALUES (?,?,?,?,?,?,?,?,?,?,?)  
        ''',i)
    idx+=1

cnn.commit()
cnn.close()