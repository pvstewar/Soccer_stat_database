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
plyr_atr.to_sql('plyr_atr', conn, if_exists='fail', index = True)
# Now to copy and replace this table to add primary key and data type
c.executescript('''
    PRAGMA foreign_keys=off;

    BEGIN TRANSACTION;
    ALTER TABLE plyr_atr RENAME TO old_plyr_atr;

    /*create new table in order to explicitly set the primary key
    and data types for each column.*/
    CREATE TABLE plyr_atr (ID INTEGER NOT NULL,
Name TEXT,
FullName TEXT NOT NULL,
Age INTEGER,
Height INTEGER,
Weight INTEGER,
PhotoUrl TEXT,
Nationality TEXT,
Overall INTEGER,
Potential INTEGER,
Growth INTEGER,
TotalStats INTEGER,
BaseStats INTEGER,
Positions TEXT,
BestPosition TEXT,
Club TEXT,
ValueEUR INTEGER,
WageEUR INTEGER,
ReleaseClause INTEGER,
ClubPosition TEXT,
ContractUntil TEXT,
ClubNumber INTEGER,
ClubJoined TEXT,
OnLoad TEXT,
NationalTeam TEXT,
NationalPosition TEXT,
NationalNumber INTEGER,
PreferredFoot TEXT,
IntReputation INTEGER,
WeakFoot INTEGER,
SkillMoves INTEGER,
AttackingWorkRate TEXT,
DefensiveWorkRate TEXT,
PaceTotal INTEGER,
ShootingTotal INTEGER,
PassingTotal INTEGER,
DribblingTotal INTEGER,
DefendingTotal INTEGER,
PhysicalityTotal INTEGER,
Crossing INTEGER,
Finishing INTEGER,
HeadingAccuracy INTEGER,
ShortPassing INTEGER,
Volleys INTEGER,
Dribbling INTEGER,
Curve INTEGER,
FKAccuracy INTEGER,
LongPassing INTEGER,
BallControl INTEGER,
Acceleration INTEGER,
SprintSpeed INTEGER,
Agility INTEGER,
Reactions INTEGER,
Balance INTEGER,
ShotPower INTEGER,
Jumping INTEGER,
Stamina INTEGER,
Strength INTEGER,
LongShots INTEGER,
Aggression INTEGER,
Interceptions INTEGER,
Positioning INTEGER,
Vision INTEGER,
Penalties INTEGER,
Composure INTEGER,
Marking INTEGER,
StandingTackle INTEGER,
SlidingTackle INTEGER,
GKDiving INTEGER,
GKHandling INTEGER,
GKKicking INTEGER,
GKPositioning INTEGER,
GKReflexes INTEGER,
STRating INTEGER,
LWRating INTEGER,
LFRating INTEGER,
CFRating INTEGER,
RFRating INTEGER,
RWRating INTEGER,
CAMRating INTEGER,
LMRating INTEGER,
CMRating INTEGER,
RMRating INTEGER,
LWBRating INTEGER,
CDMRating INTEGER,
RWBRating INTEGER,
LBRating INTEGER,
CBRating INTEGER,
RBRating INTEGER,
GKRating INTEGER);

    INSERT INTO plyr_atr SELECT * FROM old_plyr_atr;

    DROP TABLE old_plyr_atr;
    COMMIT TRANSACTION;

    PRAGMA foreign_keys=on;''')

# loading league- load the data into a Pandas DataFrame
league = pd.read_csv('league.csv')
#remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE league")
except Exception:
    pass
# write the data to a sqlite table
league.to_sql('league', conn, if_exists='fail', index = True)

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
plyr_stat.to_sql('plyr_stat', conn, if_exists='fail', index = True)

# loading teams- load the data into a Pandas DataFrame
teams = pd.read_csv('teams_fifa22.csv')
#remove table if already exists for repeated runs
try:
    c.execute("DROP TABLE teams")
except Exception:
    pass
# write the data to a sqlite table
teams.to_sql('teams', conn, if_exists='fail', index = False)
c.executescript('''
    PRAGMA foreign_keys=off;

    BEGIN TRANSACTION;
    ALTER TABLE teams RENAME TO old_teams;

    /*create new table in order to explicitly set the primary key
    and data types for each column.*/
    CREATE TABLE teams (ID INTEGER PRIMARY KEY NOT NULL,
Name TEXT NOT NULL,
League TEXT, 
LeagueId INTEGER,
Overall INTEGER,
Attack INTEGER,
Midfield INTEGER,
Defence INTEGER,
TransferBudget INTEGER,
DomesticPrestige INTEGER,
IntPrestige INTEGER,
Players INTEGER,
StartingAverageAge REAL,
AllTeamAverageAge REAL);

    INSERT INTO teams SELECT * FROM old_teams;

    DROP TABLE old_teams;
    COMMIT TRANSACTION;

    PRAGMA foreign_keys=on;''')

#View all table names
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_table=(c.fetchall())
print(available_table)

conn.commit()
conn.close()