import csv
import sqlite3

db = sqlite3.connect("ipl.db")
crsr = db.cursor()

mydata = crsr.execute("""SELECT player_id, player_name,
                    sum(case when runs_scored = 6 then 1 else 0 end) as sixes,
                    count(*) AS total, sum(case when runs_scored = 6 then 1 else 0 end)*1.0/count(*)
                    FROM BALL_BY_BALL INNER JOIN PLAYER ON PLAYER.player_id=BALL_BY_BALL.striker
                    GROUP BY player_id
                    ORDER BY sum(case when runs_scored = 6 then 1 else 0 end)*1.0/count(*) DESC
                    """)

c = mydata.fetchall()

for row in c:
    print('{},{},{},{},{}'.format(row[0], row[1], row[2], row[3], row[4]))

db.close()
