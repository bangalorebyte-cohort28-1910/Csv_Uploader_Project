# PostgreSQL

### Sources : 

https://www.youtube.com/watch?v=jNq5EAb2biY

https://www.youtube.com/watch?v=FCa4HsG-hb4


### PostgreSQL Data Types
As with all SQLAlchemy dialects, all UPPERCASE types that are known to be valid with PostgreSQL are importable from the top level dialect, whether they originate from sqlalchemy.types or from the local dialect:

from sqlalchemy.dialects.postgresql import \
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, DATE, \
    DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INTEGER, \
    INTERVAL, JSON, JSONB, MACADDR, MONEY, NUMERIC, OID, REAL, SMALLINT, TEXT, \
    TIME, TIMESTAMP, UUID, VARCHAR, INT4RANGE, INT8RANGE, NUMRANGE, \
    DATERANGE, TSRANGE, TSTZRANGE, TSVECTOR