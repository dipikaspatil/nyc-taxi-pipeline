🐳 Running PostgreSQL Locally with Docker
Local PostgreSQL instance using Docker with just one command.
```
docker run --name nyc-postgres \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=nyc_taxi \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres:15
```

🔍 Parameters
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

✅ Verify it’s running
```
docker ps
```
See the nyc-postgres container running.

🛑 Stop / Start / Remove
```
docker stop nyc-postgres
docker start nyc-postgres
docker rm -f nyc-postgres
```

🧪 Connect to the Database
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


