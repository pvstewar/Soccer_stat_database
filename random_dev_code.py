
#View all table names
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
available_table=(c.fetchall())
print(available_table)


#View table column names
c.execute("SELECT * FROM Player")
#c.execute("SELECT * FROM Player_Attributes")
col_name_list = [tuple[0] for tuple in c.description]
print(col_name_list)

#see first 5 rows
c.execute("SELECT * FROM market ORDER BY ROWID ASC LIMIT 5")
head_rows = (c.fetchall())
print(head_rows)

#show row count
c.execute("SELECT count(*) FROM Player")
row_count = (c.fetchall())
print(row_count)

#drop a table
c.execute("DROP TABLE market")

#one attempt to import csv:
c.execute("DROP TABLE Market")
create_table = '''CREATE TABLE Market(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                FullName TEXT,
                PlayerName NOT NULL,
                Affiliation TEXT,
                League TEXT,
                Jersey INTEGER,
                Birth_Date TEXT,
                Age TEXT,
                birthPlace TEXT,
                Height TEXT,
                Citizenship_1 TEXT,
                Citizenship_2 TEXT,
                Position TEXT,
                Position_2 TEXT,
                Foot TEXT,
                Agent TEXT,
                JoinedClub TEXT,
                LastExtension TEXT,
                ContractExpiration TEXT, 
                PlayerSponsor TEXT, 
                MarketValue_Euros INTEGER,
                Last_Updated_Date TEXT,
                Highest_Market_Value INTEGER,
                Highest_Market_Value_Date TEXT,
                NationalTeamCaps INTEGER);
                '''
c.execute(create_table)
#Now to open our new file:
file = open('MarkVal.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO Market (FullName, PlayerName, Affiliation, League, Jersey, Birth_Date, Age, birthPlace, Height, Citizenship_1, Citizenship_2, Position, Position_2, Foot, Agent, JoinedClub, LastExtension, ContractExpiration, PlayerSponsor, MarketValue_Euros, Last_Updated_Date, Highest_Market_Value, Highest_Market_Value_Date, NationalTeamCaps) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
c.executemany(insert_records, contents)
#conn.commit()

c.execute("DROP TABLE Market")
c.execute("CREATE TABLE Market (FullName, PlayerName, Affiliation, League, Jersey, Birth_Date, Age, birthPlace, Height, Citizenship_1, Citizenship_2, Position, Position_2, Foot, Agent, JoinedClub, LastExtension, ContractExpiration, PlayerSponsor, MarketValue_Euros, Last_Updated_Date, Highest_Market_Value, Highest_Market_Value_Date, NationalTeamCaps);") # column names in ()
with open('MarkVal.csv','r') as fin: # `with` statement available in 2.5+, csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['FullName'], i['PlayerName'], i['Affiliation'],i['League'],i['Jersey'],i['Birth_Date'],i['Age'],i['birthPlace'],i['Height'],i['Citizenship_1'],i['Citizenship_2'],i['Position'],i['Position_2'],i['Foot'],i['Agent'],i['JoinedClub'],i['LastExtension'],i['ContractExpiration'],i['PlayerSponsor'],i['MarketValue_Euros'],i['Last_Updated_Date'],i['Highest_Market_Value'],i['Highest_Market_Value_Date'],i['NationalTeamCaps']) for i in dr]
c.executemany("INSERT INTO Market (FullName, PlayerName, Affiliation, League, Jersey, Birth_Date, Age, birthPlace, Height, Citizenship_1, Citizenship_2, Position, Position_2, Foot, Agent, JoinedClub, LastExtension, ContractExpiration, PlayerSponsor, MarketValue_Euros, Last_Updated_Date, Highest_Market_Value, Highest_Market_Value_Date, NationalTeamCaps) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
conn.commit()
conn.close()
