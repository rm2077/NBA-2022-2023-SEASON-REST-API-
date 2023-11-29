from change import df
import pandas as pd
from sqlalchemy import create_engine
import sqlite3


conn = sqlite3.connect("nba.db")
engine = create_engine('sqlite://', echo=False)
df.to_sql('nba_base', con=conn, if_exists="fail", index=False)
