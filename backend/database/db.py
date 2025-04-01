from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import dotenv

from database.models.Study_stats import Study_Time

dotenv.load_dotenv('.env')
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")
DB_URL = 'sqlite:///times.db'
SUPA_DB_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'

Base = declarative_base()

engine = create_engine(SUPA_DB_URL)
try:
    session = sessionmaker(
        bind=engine, 
        autoflush=False,
        autocommit = False    
        )

    db = session()

    result = db.query(Study_Time).all()

    print('\n\nFUCK YEAAH BITCHES SUCK ME OFF\n\n')
    print('Here are the results:', result[0])
except Exception as e:
    print("Sorry bitches, gotta wait", e)
finally:
    print('DOOBIE')



