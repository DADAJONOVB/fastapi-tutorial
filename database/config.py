import sqlalchemy
import databases
import ormar


engine = sqlalchemy.create_engine("sqlite:///sqlite.db")
database = databases.Database("sqlite:///sqlite.db")
metadata = sqlalchemy.MetaData()



class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database