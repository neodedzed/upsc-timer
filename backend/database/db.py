import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import dotenv

from sqlalchemy.orm import declarative_base

Base = declarative_base()

start = datetime.datetime.now()
dotenv.load_dotenv('.env')

#SUPABASE: Get environment variables 
#for Generating DB URL
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")
DB_URL = 'sqlite:///times.db'
#Generate Supabase DB String
SUPA_DB_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'

LOCAL_DB_URL = 'sqlite:///upsc.db'

engine = create_engine(LOCAL_DB_URL)
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
        print("There is an error. Here it is.\n", e)
    finally:
        print("\nDone with the database work\n")


def print_success():
    print("Success\n")