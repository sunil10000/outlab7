import sqlite3

table_no = int(input())

def insert_team():
	team_id = int(input())
	team_name = input()
	c.execute("INSERT INTO TEAM (team_id, team_name) VALUES (?, ?);", (team_id, team_name))

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
	c.execute("""INSERT INTO MATCH (match_id, season_year, team1, team2, battedfirst, battedsecond, venue_name, 
                city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""",match_id, season_year, team1, team2, battedfirst,
                 battedsecond, venue_name,city_name, country_name, toss_winner, match_winner, toss_name, win_type, man_of_match, win_margin)

conn = sqlite3.connect('ipl.db')
crsr = conn.cursor()

