import csv
import sqlite3

db = sqlite3.connect("ipl.db")
crsr = db.cursor()

mydata = crsr.execute("""SELECT SUM(CASE WHEN battedfirst IS NOT NULL AND battedsecond IS NOT NULL THEN 1 ELSE 0 END),
                        SUM(CASE WHEN match_winner IS NOT NULL AND battedfirst = match_winner THEN 1 ELSE 0 END),
                        SUM(CASE WHEN match_winner IS NOT NULL AND battedsecond = match_winner THEN 1 ELSE 0 END)
                        FROM MATCH WHERE win_type!="NA";""")

# SELECT SUM(CASE WHEN battedsecond IS NULL THEN 1 ELSE 0 END),
#                         SUM(CASE WHEN battedfirst IS NOT NULL AND battedsecond IS NOT NULL THEN 1 ELSE 0 END),
#                         SUM(CASE WHEN match_winner IS NOT NULL AND battedfirst = match_winner THEN 1 ELSE 0 END),
#                         SUM(CASE WHEN match_winner IS NOT NULL AND battedsecond = match_winner THEN 1 ELSE 0 END)
#                     FROM MATCH
c = mydata.fetchall()

for row in c:
    print(round(row[1]*1.0/row[0], 3))
    print(round(row[2]*1.0/row[0], 3))

db.close()
