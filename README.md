# FX MARKET DATA

Proyect based on Python and sqlite to obtain, store and analyze FX data

## Set up environment: 


```bash
git clone ...
cd ...

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## HOW TO EXECUTE:

```bash
#Execute downloadpairs
python .\downloadpairs.py

#Execute bbddraw
python .\bbddraw.py

#Execute querys and modify to change the examples
python .\querys.py
```
EXPLICACION FUNCIONES

## DATABASE SQUEMA

```sql 
Create table if not exists market_exchange(
    date TEXT not null,
    close REAL not null, 
    curr1 TEXT not null, 
    curr2 TEXT not null
);
```

## VALIDATION

To validate the data there are some quality scripts that will raise an exception if the downloaded csv is not correct, the querys will be shown on the screen. 
