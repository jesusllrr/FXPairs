import pandas as pd
import sqlite3

#CONNECTION TO THE DATABASE

conn = sqlite3.connect('FXpairsJJ.db')


#EXAMPLE 1, SIMPLE QUERY
df = pd.read_sql_query("SELECT * FROM market_exchange LIMIT 10", conn)
print(df)

#EXAMPLE 2
df = pd.read_sql_query("SELECT * FROM market_exchange where curr1 = 'EUR' and curr2 = 'PLN'", conn)
print(df)


#EXAMPLE 3
df = pd.read_sql_query("SELECT close FROM market_exchange where curr1 = 'EUR' and curr2 = 'PLN' and Date = '2025-08-14'", conn)
print(df)

#EXAMPLE 4 YTD

df = pd.read_sql_query('''
SELECT Date,Close 
FROM market_exchange 
where curr1 = 'RON' and curr2 = 'PLN' and substr(Date, 1, 4) = '2025'                     
                       
''', conn)

print(df)

first = df.iloc[0]['Close']
last = df.iloc[-1]['Close']

ytd_return = (last-first) / first * 100

print(f"YTD return RON/PLN 2025: {ytd_return:.4f} %")

#EXAMPLE 5 YTD MAXMIN

df = pd.read_sql_query('''
SELECT curr1,curr2, MIN(close) as min_close, MAX(close) as max_close, 
(MAX(close)-MIN(close)) / MIN(close) * 100 as range 
FROM market_exchange 
where substr(Date, 1, 4) = '2025'  
group by 1,2                  
                       
''', conn)

print(df)



























conn.close()
