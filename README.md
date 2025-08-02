# Project: Ingesting NYC Taxi Data into PostgreSQL
#### 🎯 Steps:
```
Set up PostgreSQL in Docker
Download and process NYC Taxi data (.parquet)
Convert to .csv (optional)
Ingest into Postgres using Pandas + SQLAlchemy
Explore data using Jupyter Notebook, pgcli
Connecting pgAdmin and Postgres
```

#### 🗂️ Folder Structure
```
nyc-taxi-ingest/
├── docker-compose.yaml # Docker setup for PostgreSQL and pgAdmin
├── Dockerfile # Optional: for custom containers (not used here)
├── requirements.txt # Python dependencies
├── scripts/
│ ├── ingest_data.py # Ingests .parquet file into Postgres
│ └── convert_parquet_to_csv.py # Converts parquet to CSV (optional)
├── notebooks/
│ └── explore_data.ipynb # Jupyter Notebook to explore data
├── data/
│ └── yellow_tripdata_2023-01.parquet # NYC taxi dataset (downloaded)
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo & Set Up

```
bash
git clone https://github.com/dipikaspatil/nyc-taxi-ingest.git
cd nyc-taxi-ingest
```

### 2️⃣ Install Python Environment
```
Note: Because of the recent Python security model changes (especially with Homebrew's Python 3.12+), installing directly via pip3 can result in externally-managed-environment errors.
✅ The best and safest fix: Use a virtual environment
This avoids permission errors and doesn't affect your system Python.

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Launch PostgreSQL with Docker
```
docker-compose up -d
```
PostgreSQL runs on localhost:5432
pgAdmin runs on localhost:8080
Login: admin@admin.com / admin

### 4️⃣ Download the Dataset
```
cd data
wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
cd ..
```

### 5️⃣ Convert Parquet to CSV
```
python scripts/convert_parquet_to_csv.py
```

### 6️⃣ Ingest Data into Postgres
```
python scripts/ingest_data.py
```
This will:
Connect to Docker PostgreSQL
Create table yellow_taxi_data
Insert all rows from the .csv file

### 📊 Explore Data in Jupyter
```
jupyter notebook
```
Open notebooks/explore_data.ipynb and run:
```
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:postgres@localhost:5432/nyc_taxi')
df = pd.read_sql("SELECT * FROM yellow_taxi_data LIMIT 100", engine)
df.head()

# Get Schema
print(pd.io.sql.get_schema(df, name="yellow_taxi_data", con=engine))
```

### 🧪 Connect to the Database
Connect using:
```
pgcli:
pgcli -h localhost -p 5432 -U postgres -d nyc_taxi

Node: if needed install pgcli using "brew install pgcli"
🧠 Handy Tips
Action	Command
List tables	    \dt
Describe table	\d tablename
Quit	          \q
Run query	      SELECT * FROM your_table;
```

```
Or Python:
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:postgres@localhost:5432/nyc_taxi")
```

### 🎥 Connecting pgAdmin and Postgres
```
Open pgAdmin in Browser
Go to: http://localhost:5050

Email: admin@admin.com
Password: admin

Register Your Postgres Server
In pgAdmin UI:
Right-click on Servers → Register → Server

Fill in details:
🔹 General tab
Name: nyc_postgres
🔹 Connection tab
Host: postgres ← (this is the name of the service in docker-compose)
Port: 5432
Username: postgres
Password: postgres
Save password: ✅
```
