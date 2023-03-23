import pandas as pd
import time
import gzip
import json

t0 = time.time()
df = pd.read_json('data/raw/Sports_and_Outdoors_5.json', lines=True)
t1 = time.time()

print(df.head())
print(f"Time to process dataframe: {t1-t0:.2f} seconds")