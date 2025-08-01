import pandas as pd

df = pd.read_parquet('data/yellow_tripdata_2023-01.parquet')
df.to_csv('data/yellow_tripdata_2023-01.csv', index=False)
print("CSV saved to data/yellow_tripdata_2023-01.csv")
