import sqlite3

conn = sqlite3.connect('ipl.db')
crsr = conn.cursor()

crsr.execute("CREATE TABLE TEAM (team_id INT PRIMARY KEY, team_name TEXT)")

crsr.execute("CREATE TABLE MATCH (match_id INT NOT NULL , team1 INT, team2 INT,\
			battedfirst INT, battedsecond INT,\
			FOREIGN KEY (team1) REFERENCES TEAM(team_id),\
			FOREIGN KEY (team2) REFERENCES TEAM(team_id),\
			FOREIGN KEY (battedfirst) REFERENCES TEAM(team_id),\
			FOREIGN KEY (battedsecond) REFERENCES TEAM(team_id))")

			# toss_winner INT, match_winner INT, toss_name TEXT, win_type TEXT, man_of_match INT,\
			# win_margin INT,PRIMARY KEY(match_id),\
			 # venue_name TEXT, city_name TEXT,country_name TEXT,, season_year INT

crsr.execute("CREATE TABLE PLAYER (player_id INT PRIMARY KEY, player_name TEXT,\
			dob TIMESTAMP, batting_hand TEXT, bowling_skill TEXT, country_name TEXT)")

crsr.execute("CREATE TABLE PLAYER_MATCH (playermatch_key BIGINT PRIMARY KEY,\
			match_id INT, player_id INT,\
			batting_hand TEXT, bowling_skill TEXT, role_desc TEXT, team_id INT,\
			FOREIGN KEY (match_id) REFERENCES MATCH(match_id),\
			FOREIGN KEY (player_id) REFERENCES PLAYER(player_id),\
			FOREIGN KEY (team_id) REFERENCES TEAM(team_id))")

crsr.execute("CREATE TABLE BALL_BY_BALL (match_id INT,innings_no INT, over_id INT,\
			ball_id INT, striker_batting_position INT, runs_scored INT, extra_runs INT,\
			out_type TEXT, striker INT, non_striker INT,bowler INT,\
			PRIMARY KEY (match_id, innings_no,over_id,ball_id),\
			FOREIGN KEY (match_id) REFERENCES MATCH(match_id),\
			FOREIGN KEY (striker) REFERENCES PLAYER(player_id),\
			FOREIGN KEY (non_striker) REFERENCES PLAYER(player_id),\
			FOREIGN KEY (bowler) REFERENCES PLAYER(player_id))")

conn.commit()
conn.close()
