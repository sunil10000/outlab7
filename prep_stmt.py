import sqlite3

table_no = int(input())

def insert_team():
	team_id = int(input())
	team_name = input()
	conn = sqlite3.connect('ipl.db')
	crsr = conn.cursor()
	crsr.execute("INSERT INTO TEAM (team_id, team_name) VALUES (?, ?);", (team_id, team_name))
	conn.commit()
	conn.close()

def insert_match():
	match_id = int(input())
	season_year = int(input())
	team1 = int(input())
	team2 = int(input())
	battedfirst = int(input())
	battedsecond = int(input())
	venue_name = input()
	city_name = input()
	country_name = input()
	toss_winner = input()
	match_winner = input()
	toss_name = input()
	win_type = input()
	man_of_match = int(input())
	win_margin = int(input())
	conn = sqlite3.connect('ipl.db')
	crsr = conn.cursor()
	crsr.execute("""INSERT INTO MATCH (match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name, 
                city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
                 (match_id, season_year, team1, team2, battedfirst,
                 battedsecond, venue_name,city_name, country_name, toss_winner,
                 match_winner, toss_name,
                 win_type, man_of_match, win_margin))
	conn.commit()
	conn.close()

def insert_player():
	player_id  = int(input())
	player_name = input()
	dob = input()
	batting_hand = input()
	bowling_skill = input()
	country_name = input()
	conn = sqlite3.connect('ipl.db')
	crsr = conn.cursor()
	crsr.execute("""INSERT INTO PLAYER (player_id, player_name, dob, batting_hand, 
            bowling_skill, country_name) VALUES (?, ?, ?, ?, ?, ?);""",
            (player_id, player_name, dob, batting_hand,bowling_skill, country_name))
	conn.commit()
	conn.close()


def insert_player_match():
	playermatch_key = int(input())
	match_id = int(input()) 
	player_id = int(input())
	batting_hand = input()
	bowling_skill = input()
	role_desc = input()
	team_id = int(input())
	conn = sqlite3.connect('ipl.db')
	crsr = conn.cursor()
	crsr.executemany("""INSERT INTO PLAYER_MATCH (playermatch_key, match_id, player_id, batting_hand, bowling_skill, role_desc, 
            team_id) VALUES (?, ?, ?, ?, ?, ?, ?);""",
            (playermatch_key, match_id, player_id, batting_hand, bowling_skill, role_desc, team_id))
	conn.commit()
	conn.close()

def insert_ball():
	match_id = int(input())
	innings_no = int(input())
	over_id = int(input())
	ball_id = int(input())
	striker_batting_position = int(input())
	runs_scored = int(input())
	extra_runs = int(input())
	out_type = input()
	striker = int(input())
	non_striker = int(input())
	bowler = int(input())
	conn = sqlite3.connect('ipl.db')
	crsr = conn.cursor()
	crsr.execute("""INSERT INTO BALL_BY_BALL (match_id, innings_no, over_id, ball_id, striker_batting_position, runs_scored, extra_runs,\
    out_type, striker, non_striker, bowler) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",
	    (match_id, innings_no, over_id, ball_id,
	    striker_batting_position, runs_scored, extra_runs,
	    out_type, striker, non_striker, bowler))
	conn.commit()
	conn.close()



if (table_no==1):
	insert_team()
elif (table_no==2):
	insert_player()
elif (table_no==3):
	insert_match()
elif (table_no==4):
	insert_player_match()
elif (table_no==5):
	insert_ball()
else:
	print("wrong_input")
