import os
from dotenv import load_dotenv
from db import connect
import psycopg2

load_dotenv()  # loads variables from .env

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

if __name__=="__main__":
    try:
        conn = connect()
        print("connected succesfully")
        conn.close()
    except Exception as e:
        print("Error: ", e)