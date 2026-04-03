import psycopg2

def connect():
    return psycopg2.connect(
        dbname="grocery_db",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )

if __name__=="__main__":
    try:
        conn = connect()
        print("connected succesfully")
        conn.close()
    except Exception as e:
        print("Error: ", e)