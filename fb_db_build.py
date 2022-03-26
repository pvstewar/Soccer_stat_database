import csv
import sqlite3
import pandas as pd
#first we need to create the db
file = "fb.db"
  
conn = sqlite3.connect('fb.db')
c = conn.cursor()

# loading plyr_atr- load the data into a Pandas DataFrame
plyr_atr = pd.read_csv('players_fifa22.csv')
#try remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE plyr_atr")
except Exception:
    pass
# write the data to a sqlite table
plyr_atr.to_sql('plyr_atr', conn, if_exists='fail', index = False)

# loading league- load the data into a Pandas DataFrame
league = pd.read_csv('league.csv')
#remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE league")
except Exception:
    pass
# write the data to a sqlite table
league.to_sql('league', conn, if_exists='fail', index = False)

# loading plyr_shot- load the data into a Pandas DataFrame
plyr_shot = pd.read_csv('plyr_shot.csv')
#remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE plyr_shot")
except Exception:
    pass
# write the data to a sqlite table
plyr_shot.to_sql('plyr_shot', conn, if_exists='fail', index = False)

# loading plyr_stat- load the data into a Pandas DataFrame
plyr_stat = pd.read_csv('plyr_stat.csv')
#remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE plyr_stat")
except Exception:
    pass
# write the data to a sqlite table
plyr_stat.to_sql('plyr_stat', conn, if_exists='fail', index = False)

# loading teams- load the data into a Pandas DataFrame
teams = pd.read_csv('teams_fifa22.csv')
#remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE teams")
except Exception:
    pass
# write the data to a sqlite table
teams.to_sql('teams', conn, if_exists='fail', index = False)

#View all table names
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_table=(c.fetchall())
print(available_table)

conn.commit()
conn.close()