import sqlite3

connection = sqlite3.connect("ipl.db");
cursor = connection.cursor();

sql_team = '''CREATE TABLE TEAM(
              team_id         int,
              team_name       text,
              PRIMARY KEY(team_id)
)'''

sql_player = '''CREATE TABLE PLAYER(
                player_id       int,
                player_name     text,
                dob             TIMESTAMP,
                batting_hand    text,
                bowling_skill   text,
                country_name    text,
                PRIMARY KEY(player_id)
)'''

sql_match = '''CREATE TABLE MATCH(
               match_id         int,
               season_year      int,
               team1            int,
               team2            int,
               battedfirst      int,
               battedsecond     int,
               venue_name       text,
               city_name        text,
               country_name     text,
               toss_winner      int,
               match_winner     int,
               toss_name        text,
               win_type         text,
               man_of_match     int,
               win_margin       int,
               PRIMARY KEY(match_id),
               FOREIGN KEY (team1) REFERENCES TEAM (team_id),
               FOREIGN KEY (team2) REFERENCES TEAM (team_id),
               FOREIGN KEY (battedfirst) REFERENCES TEAM (team_id),
               FOREIGN KEY (battedsecond) REFERENCES TEAM (team_id)
)'''

sql_player_match = '''CREATE TABLE PLAYER_MATCH(
                      playermatch_key       int,
                      match_id              int,
                      player_id             int,
                      batting_hand          text,
                      bowling_skill         text,
                      role_desc             text,
                      team_id               int,
                      PRIMARY KEY (playermatch_key),
                      FOREIGN KEY (match_id) REFERENCES MATCH (match_id),
                      FOREIGN KEY (player_id) REFERENCES PLAYER (player_id),
                      FOREIGN KEY (team_id) REFERENCES TEAM (team_id)
)'''

sql_ball_by_ball = '''CREATE TABLE BALL_BY_BALL(
                      match_id                  int,
                      innings_no                int,
                      over_id                   int,
                      ball_id                   int,
                      striker_batting_position  int,
                      runs_scored               int,
                      extra_runs                int,
                      out_type                  text,
                      striker                   int,
                      non_striker               int,
                      bowler                    int,
                      PRIMARY KEY (match_id, innings_no, over_id, ball_id),
                      FOREIGN KEY (match_id) REFERENCES MATCH (match_id),
                      FOREIGN KEY (striker) REFERENCES PLAYER (player_id),
                      FOREIGN KEY (non_striker) REFERENCES PLAYER (player_id),
                      FOREIGN KEY (bowler) REFERENCES PLAYER (player_id)
)'''

cursor.execute(sql_team);
cursor.execute(sql_player)
cursor.execute(sql_match)
cursor.execute(sql_player_match)
cursor.execute(sql_ball_by_ball)

connection.commit()
connection.close()

