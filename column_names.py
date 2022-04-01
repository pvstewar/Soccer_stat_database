import sqlite3
conn = sqlite3.connect('fb.db')
c = conn.cursor()
c.execute('select * from plyr_stat')
names = [description[0] for description in c.description]
conn.close()
with open("plyr_stat_c_names.txt", "w") as output:
    output.write(str(names))