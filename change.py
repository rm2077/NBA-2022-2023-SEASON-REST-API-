import pandas as pd
from data_scraping import df

'''rows, cols = df.shape
for i in range(rows):
    print("".join(df["Player"][i].split()))'''

df["Player"] = df["Player"].str.replace(" ", "").str.lower()
print(df.head())
