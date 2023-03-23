from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.state import State
from models.engine.db_storage import DBStorage

        
s = DBStorage()

print(s)
