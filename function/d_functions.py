import yfinance as yf
import pandas as pd



def download_pairs(pairs, ini, fin, dataframes):
    '''
    Return dataframes {}
    Pairs [] with the possible currencies cross-paired
    ini, fin datetime meaning start and end of the time lapse we obtain data
    Upload dataframes with FX data obtain from yfinance

    '''
    for par in pairs:
        nombre_df = par.replace("=X", "_X")

        df = yf.download(par, ini, fin)

        if not df.empty and (len(df)) != 1:
            df = df[['Close']].reset_index()
            df['Date'] = pd.to_datetime(df['Date']).dt.date
            df.columns = ['Date', 'Close']
            dataframes[nombre_df] = df

        #if there is no data or the data is not complete we will calculate it
        else:
            df = pd.DataFrame()
            dataframes[nombre_df] = df
    
    return dataframes


def download_usd(usd_pairs, ini, fin, usd_data):
    '''
    Return usd_data {}
    usd_pairs [] with the possible currencies cross-paired (USDXXX)
    ini, fin datetime meaning start and end of the time lapse we obtain data
    Upload usd_data with FX data obtain from yfinance
    '''
    for par in usd_pairs:
        curr = par[:3]
        df = yf.download(par, ini, fin)

        if not df.empty:
            df = df[['Close']].reset_index()
            df['Date'] = pd.to_datetime(df['Date']).dt.date
            df.columns = ['Date', par]
            usd_data[curr] = df
    
    return usd_data


def calc_pair(mon1, mon2, usd_d):
    '''
    Return merged
    mon1 mon2 name of the currencies
    Calculate FX values based on USD
    '''
    df_mon_1 = usd_d[mon1]
    df_mon_2 = usd_d[mon2]
    df_mon_1 = df_mon_1.rename(columns={f'{mon1}USD=X': mon1})
    df_mon_2 = df_mon_2.rename(columns={f'{mon2}USD=X': mon2})

    merged = pd.merge(df_mon_1, df_mon_2, on='Date', how='inner')

    merged['Close'] = merged[mon1] / merged[mon2]

    return merged[['Date', 'Close']]

def complete_pairs(pairs, dataframes, usd_data):
    '''
    Return dataframes {}
    Pairs [] with the possible currencies cross-paired
    usd_data {} dictionary df values FX (USDXXX) [Date | Close]
    Complete dataframes missing values

    '''
    for par in pairs:
        mon1 = par[:3]
        mon2 = par[3:6]
    
        nombre_df = f"{mon1}{mon2}_X"

        if dataframes[nombre_df].empty:
            df_calc = calc_pair(mon1, mon2, usd_data)
            if not df_calc.empty:
                dataframes[nombre_df] = df_calc
            
    
    return dataframes

def data_union(all_df, dataframes):
    '''
    return final_df 
    all_df = []
    dataframes {} dictionary with FX data [Date|Close]
    add two columns with the currencies (staged in the name of the df) and append all in one df
    '''
    for name, df in dataframes.items():
        curr1 = name[:3]
        curr2 = name[3:6]

        df_copy = df.copy()
        df_copy['curr1'] = curr1
        df_copy['curr2'] = curr2

        all_df.append(df_copy)

    final_df = pd.concat(all_df,ignore_index=True)

    return final_df
