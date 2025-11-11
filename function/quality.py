import pandas as pd
import re



def q_format(df):
    '''
    Format validation of the fields Date (YYYY-MM-DD) and curr (CHAR(3))
    '''
    reg_date = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    if not df['Date'].apply(lambda x: bool(reg_date.match(str(x)))).all():
        raise ValueError('Format on Date is not correct')
    
    if not df['curr1'].apply(lambda x: len(str(x)) == 3).all():
        raise ValueError('Format on curr1 is not correct')
    
    if not df['curr2'].apply(lambda x: len(str(x)) == 3).all():
        raise ValueError('Format on curr2 is not correct')
    

def q_duplicates(df):
    '''
    Duplicate fields validation
    '''

    if df.duplicated(subset=['Date', 'curr1', 'curr2']).any():
        raise ValueError('The data contains duplicates')

