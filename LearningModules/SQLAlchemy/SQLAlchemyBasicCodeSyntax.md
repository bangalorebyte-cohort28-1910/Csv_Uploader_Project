# SQLAlchemy basic code syntax reference

### To create a new database using PostgreSQL:

If not done, do this step first

```
pip install sqlalchemy_utils
```

then, create a file [something like create_database.py]

```
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

engine = create_engine('postgresql+psycopg2://{username}:{password}@localhost/{new_database_name}')
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))
```
