from contextlib import contextmanager
import os
import pymysql

@contextmanager
def db_conn():
    conn = None

    try:
        host = os.environ.get("DB_HOST")
        user = os.environ.get("DB_USER")
        pw = os.environ.get("DB_PASSWORD")
        db_name = os.environ.get("DB_NAME")


        conn = pymysql.connect(host=host, user=user, password=pw, database=db_name)
        csr = conn.cursor()
        yield csr
        conn.commit()
        csr.close()
    except Exception as e:
        if conn is not None:
            conn.rollback()
        print(f"Database connection failed: {e}")
        raise e
    finally:
        if conn:
            conn.close()


query_string = """create table if not exists groceries(
    id VARCHAR(36) primary key, 
    name VARCHAR(100) not null,
    price numeric(10,2) not null
)"""

with db_conn() as csr:
    csr.execute(query_string)
    print("Database created.")