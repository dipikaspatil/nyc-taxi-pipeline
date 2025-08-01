import pandas as pd
from time import time
from sqlalchemy import create_engine

# Connect to Postgres in Docker
engine = create_engine('postgresql://postgres:postgres@localhost:5432/nyc_taxi')

df_iter = pd.read_csv('data/yellow_tripdata_2023-01.csv', iterator=True, chunksize=100000)
df = next(df_iter)
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Create table
df.head(0).to_sql('yellow_taxi_data', engine, if_exists='replace', index=False)

# Insert data
df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append", index=False)

# Insert remaining data in table
while True:
    df = next(df_iter)
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    t_start = time()
    df.to_sql(name="yellow_taxi_data", con=engine, if_exists="append", index=False)
    t_end = time()
    print("Inserted another chunk... took %3f seconds " % (t_end - t_start))

print("Data ingested successfully.")

