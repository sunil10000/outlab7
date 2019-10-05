import csv
import sqlite3

db = sqlite3.connect("ipl.db")
crsr = db.cursor()

mydata= crsr.execute("SELECT runs_scored FROM ball_by_ball GROUP BY match_id")