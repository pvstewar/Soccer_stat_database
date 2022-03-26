import csv
import sqlite3
import pandas as pd

conn = sqlite3.connect('fb.db')
c = conn.cursor()

#View all table names
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_table=(c.fetchall())
print(available_table)

#View table column names
c.execute("SELECT * FROM league")
col_name_league = [tuple[0] for tuple in c.description]
print("league columns:", col_name_league)
#show row count
c.execute("SELECT count(*) FROM league")
league_row_count = (c.fetchall())
print("league row count:", league_row_count)

c.execute("SELECT * FROM plyr_atr")
col_name_plyr_atr = [tuple[0] for tuple in c.description]
print("Atr columns:", col_name_plyr_atr)
#show row count
c.execute("SELECT count(*) FROM plyr_atr")
plyr_atr_row_count = (c.fetchall())
print("plyr_atr row count:", plyr_atr_row_count)

c.execute("SELECT * FROM plyr_shot")
col_name_plyr_shot = [tuple[0] for tuple in c.description]
print("plyr_shot columns:", col_name_plyr_shot)
#show row count
c.execute("SELECT count(*) FROM plyr_shot")
plyr_shot_row_count = (c.fetchall())
print("plyr_shot row count:", plyr_shot_row_count)

c.execute("SELECT * FROM plyr_stat")
col_name_plyr_stat = [tuple[0] for tuple in c.description]
print("plyr_stat columns:", col_name_plyr_stat)
#show row count
c.execute("SELECT count(*) FROM plyr_stat")
plyr_stat_row_count = (c.fetchall())
print("plyr_stat row count:", plyr_stat_row_count)

c.execute("SELECT * FROM teams")
col_name_plyr_teams = [tuple[0] for tuple in c.description]
print("teams columns:", col_name_plyr_teams)
#show row count
c.execute("SELECT count(*) FROM teams")
teams_row_count = (c.fetchall())
print("teams row count:", teams_row_count)

conn.close()