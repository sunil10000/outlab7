import csv
import sqlite3

db = sqlite3.connect("ipl.db")
crsr = db.cursor()

mydata = crsr.execute("""SELECT venue_name, SUM(runs_scored)*1.0/COUNT(distinct MATCH.match_id) FROM
                      BALL_BY_BALL INNER JOIN MATCH ON MATCH.match_id = BALL_BY_BALL.match_id GROUP BY venue_name""")
c = mydata.fetchall()

for row in c:
    print(row)

db.close()
