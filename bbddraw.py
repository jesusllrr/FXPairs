import pandas as pd
import sqlite3
from function.quality import q_format, q_duplicates


PATH_CSV = 'FXpairs.csv'
PATH_BBDD = 'FXpairsJJ.db'
#Read csv

df = pd.read_csv(PATH_CSV)

# Clean data, we import a quality process.

q_format(df)
q_duplicates(df)
#Connect and create database

conn = sqlite3.connect(PATH_BBDD)

cursor = conn.cursor()

create_table = '''
Create table if not exists market_exchange(
    date TEXT not null,
    close REAL not null, 
    curr1 TEXT not null, 
    curr2 TEXT not null
);
'''

conn.execute(create_table)

df.to_sql("market_exchange", conn, if_exists="replace", index=False)

conn.commit()
conn.close()




