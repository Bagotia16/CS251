import sqlite3
import sys

cnn = sqlite3.connect('ipl.db')
cursor = cnn.cursor()


if sys.argv[1]=="1":
    cursor.execute('''INSERT INTO TEAM (team_id, team_name)
                      VALUES (?,?)
    ''', (int(sys.argv[2]), sys.argv[3]))

elif sys.argv[1]=="2":
    # print("a")
    cursor.execute('''INSERT INTO PLAYER (player_id, player_name, dob, batting_hand, bowling_skill, country_name)
                      VALUES (?, ?, ?, ?, ?, ?)
    ''', (int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]))
    # cnn.commit()
    # cnn.close()

elif sys.argv[1]=="3":
    cursor.execute('''INSERT INTO MATCH (match_id, season_year, team1, team2, 
                                         battedfirst, battedsecond, venue_name,
                                         city_name, country_name, toss_winner,
                                         match_winner, toss_name, win_type,
                                         man_of_match, win_margin)
                      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), 
         int(sys.argv[7]), sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11],
         sys.argv[12], sys.argv[13], sys.argv[14], sys.argv[15], sys.argv[16])
    )

elif sys.argv[1]=="4":
    cursor.execute('''INSERT INTO PLAYER_MATCH (playermatch_key, match_id, player_id,
                                                batting_hand, bowling_skill,
                                                role_desc, team_id)
                      VALUES (?,?,?,?,?,?,?)
    ''', (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6], sys.argv[7], int(sys.argv[8]))
    )

elif sys.argv[1]=="5":
    cursor.execute('''INSERT INTO BALL_BY_BALL (match_id, innings_no, over_id, ball_id,
                                                striker_batting_position, runs_scored, extra_runs,
                                                out_type, striker, non_striker, bowler)
                      VALUES (?,?,?,?,?,?,?,?,?,?,?)
    ''', (int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6], 
          int(sys.argv[7]), int(sys.argv[8]), sys.argv[9], int(sys.argv[10]), int(sys.argv[11]),
          int(sys.argv[12]))
    )


cnn.commit()
cnn.close()
