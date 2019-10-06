import csv
import sqlite3

db = sqlite3.connect("ipl.db")
crsr = db.cursor()

mydata = crsr.execute("""SELECT player_id, player_name, 
                    COUNT(BALL_BY_BALL.match_id)*1.0/COUNT(distinct BALL_BY_BALL.match_id),
                    DENSE_RANK () OVER (ORDER BY COUNT(BALL_BY_BALL.match_id)*1.0/COUNT(distinct BALL_BY_BALL.match_id) DESC)
                    FROM BALL_BY_BALL INNER JOIN PLAYER ON PLAYER.player_id=BALL_BY_BALL.striker GROUP BY player_id
                    """)

c = mydata.fetchall()

for row in c:
    if row[3] <= 10:
        print('{},{},{}'.format(row[0], row[1], row[2]))
    else:
        break

db.close()
