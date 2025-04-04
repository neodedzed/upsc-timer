import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import dotenv

from database.models.Study_stats import Study_Time
start = datetime.datetime.now()
dotenv.load_dotenv('.env')

#Get environment variables for Generating DB URL
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")
DB_URL = 'sqlite:///times.db'
# print(datetime.datetime.now()-start, "For Variables")
#Generate Supabase DB String
SUPA_DB_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'

Base = declarative_base()

engine = create_engine(SUPA_DB_URL)
print(datetime.datetime.now()-start, "For Creating engine")
session = sessionmaker(
        bind=engine, 
        autoflush=False,
        autocommit = False    
        )

def get_db():
    try:
        db = session()
        print('Yielding database')
        # print(datetime.datetime.now()-start, "For creating engine")
        yield db
    except Exception as e:
        print("There is an error. Here it is.", e)
    finally:
        print("Let's fucking gooo!!")



