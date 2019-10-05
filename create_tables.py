import sqlite3

conn = sqlite3.connect('ip1.db')
crsr = conn.cursor()

crsr.execute("CREATE TABLE TEAM (team_id INT, team_name TEXT)")
crsr.execute("CREATE TABLE PLAYER_MATCH (plaermatch_key BIGINT, match_id INT,player_id INT,\
	batting_hand TEXT, bowling_skill TEXT, role_desc TEXT, team_id INT)")
crsr.execute("CREATE TABLE MATCH (match_id INT, season_year INT, team1 INT, team2 INT)")
crsr.execute("CREATE TABLE PLAYER (player_id INT, player_name TEXT,dob TIMESTAMP,\
	batting_hand TEXT, bowling_skill TEXT, country_name TEXT)")
crsr.execute("CREATE TABLE BLL_BY_BLL (team_id INT, team_name TEXT")
