import yfinance as yf
import pandas as pd
from itertools import permutations
from datetime import datetime, timedelta
from function.d_functions import download_pairs,download_usd,complete_pairs,data_union

#obtain all possible pairs and store them in 'pairs'

currencies = ["NOK", "EUR", "SEK", "PLN", "RON", "DKK", "CZK"]
pairs = [f"{mon1}{mon2}=X" for mon1, mon2 in permutations(currencies, 2)]


#dictionary with the dataframes
dataframes = {}

#download parameters and download directly
fin = datetime.now()
ini = fin - timedelta(days = 365)


#FUNCTION 1

dataframes = download_pairs(pairs,ini,fin, dataframes)
    

#Download the usd data to calculate the rest 

usd_pairs = [f"{m}USD=X" for m in currencies]
usd_data = {}


#FUNCTION 2 
usd_data = download_usd(usd_pairs, ini, fin, usd_data)


#Complete the rest of the pairs 
#FUNCTION 3

dataframes = complete_pairs(pairs, dataframes, usd_data)
#Unify all in one csv

#FUNCTION 4 

all_df = []

final_df = data_union(all_df, dataframes)

final_df.to_csv('FXpairs.csv', index=False)
