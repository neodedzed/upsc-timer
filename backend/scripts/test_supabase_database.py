import psycopg2
from dotenv import load_dotenv
import os
import sqlalchemy

# Load environment variables from .env
load_dotenv()

# Fetch variables
print('\n------------------First Part-------------\n')

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")
print(f'''
USER = {USER}
PASSWORD = {PASSWORD}
HOST = {HOST}
PORT = {PORT}
DBNAME = {DBNAME}
''')
# DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.yfczyzrsrvhovoetxbiy.supabase.co:5432/postgres
# Connect to the database
try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        dbname=DBNAME
    )
    print("Connection successful!")
    
    # Create a cursor to execute SQL queries
    cursor = connection.cursor()
    
    # Example query
    cursor.execute("SELECT * FROM study_sessions;")
    result = cursor.fetchall()
    print("Current Time:", result)

    # Close the cursor and connection
    cursor.close()
    connection.close()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect: {e}")


# print('\n------------------Second Part-------------\n')
# USER_direct = os.getenv("user_direct")
# PASSWORD_direct = os.getenv("password_direct")
# HOST_direct = os.getenv("host_direct")
# PORT_direct = os.getenv("port_direct")
# DBNAME_direct = os.getenv("dbname_direct")
# print(f'''
# USER_direct = {USER_direct}
# PASSWORD_direct = {PASSWORD_direct}
# HOST_direct = {HOST_direct}
# PORT_direct = {PORT_direct}
# DBNAME_direct = {DBNAME_direct}
# ''')
# try:
#     connection = psycopg2.connect(
#         user=USER_direct,
#         password=PASSWORD_direct,
#         host=HOST_direct,
#         port=PORT_direct,
#         dbname=DBNAME_direct
#     )
#     print("Connection successful!")
    
#     # Create a cursor to execute SQL queries
#     cursor = connection.cursor()
    
#     # Example query
#     cursor.execute("SELECT NOW();")
#     result = cursor.fetchone()
#     print("Current Time:", result)

#     # Close the cursor and connection
#     cursor.close()
#     connection.close()
#     print("Connection closed.")

# except Exception as e:
#     print(f"Failed to connect: {e}")

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from database.models.Study_stats import Study_Time
# DATABASE_URL='postgresql://postgres:z24yUT95PairiZPd@db.yfczyzrsrvhovoetxbiy.supabase.co:5432/postgres?sslmode=require'

# engine = create_engine(DATABASE_URL)
# session = sessionmaker(bind=engine)

# SessionLocal = session()

# print(SessionLocal.query(Study_Time).all())

