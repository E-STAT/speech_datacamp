# Import create_engine
from sqlalchemy import create_engine
# Create an engine that connects to the census.sqlite file: engine
engine = create_engine("sqlite:///census.sqlite")

# Print table names
print(engine.table_names())


# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine, Table, MetaData

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = MetaData()

# Reflect census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))
