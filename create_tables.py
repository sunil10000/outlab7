import sqlite3

conn = sqlite3.connect('ip1.db')
crsr = conn.cursor()

crsr.execute("CREATE TABLE TEAM (team_id INT, team_name TEXT)")
crsr.execute("CREATE TABLE PLAYER_MATCH (plaermatch_key BIGINT, match_id INT,player_id INT,\
	batting_hand TEXT, bowling_skill TEXT, role_desc TEXT, team_id INT)")
crsr.execute("CREATE TABLE MATCH (match_id INT, season_year INT, team1 INT, team2 INT,\
	battedfirst INT, battedsecond INT, venue_name TEXT, city_name TEXT,country_name TEXT,\
	toss_winner TEXT, match_winner TEXT, toss_name TEXT, win_type TEXT, man_of_match INT,\
	win_margin INT)")
crsr.execute("CREATE TABLE PLAYER (player_id INT, player_name TEXT,dob TIMESTAMP,\
	batting_hand TEXT, bowling_skill TEXT, country_name TEXT)")
crsr.execute("CREATE TABLE BALL_BY_BALL (match_id INT,innings_no INT, over_id INT,\
	ball_id INT, striker_batting_position INT, runs_scored INT, extra_runs INT,\
	out_type TEXT, striker INT, non_striker INT)")
