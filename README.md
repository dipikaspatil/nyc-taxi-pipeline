# 🐳 Running PostgreSQL Locally with Docker
#### Local PostgreSQL instance using Docker with just one command.
```
docker run --name nyc-postgres \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=nyc_taxi \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres:15
```

#### 🔍 Parameters
```
Option	   Description
--name     nyc-postgres	Name of the container
-e         POSTGRES_USER=myuser	Creates a PostgreSQL user
-e         POSTGRES_PASSWORD=...	Sets password for the user
-e         POSTGRES_DB=nyc_taxi	Creates a default database
-p         5432:5432	Maps host to container port
-v         pgdata:/...	Persists data with a Docker volume
-d         postgres:15	PostgreSQL image version
```

#### ✅ Verify it’s running
```
docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                                         NAMES
435e6681c693   postgres:15   "docker-entrypoint.s…"   13 seconds ago   Up 12 seconds   0.0.0.0:5432->5432/tcp, [::]:5432->5432/tcp   nyc-postgres
```
See the nyc-postgres container running.

#### 🛑 Stop / Start / Remove
```
docker stop nyc-postgres
docker start nyc-postgres
docker rm -f nyc-postgres
```

#### 🧪 Connect to the Database
Connect using:
```
pgcli:
pgcli -h localhost -p 5432 -U myuser -d nyc_taxi
```

```
Or Python:
from sqlalchemy import create_engine
engine = create_engine("postgresql://myuser:mypassword@localhost:5432/nyc_taxi")
```
# Exploring the NY Taxi dataset

#### 🚕 What Is the NYC Taxi Dataset?

```
This is a public dataset published by the NYC Taxi and Limousine Commission (TLC), which includes millions of trip records:

Pickup and drop-off datetime & locations

Trip distances
Fare amounts
Payment types
Passenger counts

It’s available monthly and for multiple years.
````

#### ✅ Step 1: Download a Sample Dataset
Start with a small dataset to avoid memory issues during early exploration.

Download a monthly Parquet or CSV file, like:

```
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
```
👉 File will be around 75–200 MB (compressed) and contain millions of rows.

#### ✅ Step 2: Explore in Python (Pandas)

```
import pandas as pd

df = pd.read_csv('yellow_tripdata_2023-01.csv')

print(df.head())
print(df.dtypes)
print(df.describe())
```

Columns:

Date/time columns: tpep_pickup_datetime, tpep_dropoff_datetime
Numerical: trip_distance, fare_amount
Categorical: payment_type, VendorID

#### ✅ Step 3: Clean the Data
Some examples of what you might clean:

```
# Convert datetime columns
df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

# Remove invalid rows
df = df[df['trip_distance'] > 0]
df = df[df['fare_amount'] > 0]
```

#### ✅ Step 4: Visualize
Using tools like matplotlib, seaborn, or plotly:

```
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['trip_distance'], bins=50)
plt.show()
```

Or:

```
df['trip_duration'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
df['trip_duration'].hist(bins=50)
```

#### ✅ Step 5: Load into PostgreSQL (optional)
If you’re running Postgres in Docker (as we discussed), you can load the data using psycopg2, sqlalchemy, or pgcli:

```
pgcli -h localhost -U myuser -d mydb
```
And from Python:

```
from sqlalchemy import create_engine

engine = create_engine("postgresql://myuser:mypassword@localhost:5432/mydb")
df.to_sql("nyc_taxi", engine, if_exists="replace", index=False)
```

#### ✅ Step 6: SQL Exploration (examples)

```
SELECT COUNT(*) FROM nyc_taxi;
SELECT AVG(trip_distance) FROM nyc_taxi;
SELECT passenger_count, AVG(fare_amount)
FROM nyc_taxi
GROUP BY passenger_count;
```
