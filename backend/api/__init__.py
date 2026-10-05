import sqlite3
from sqlite3 import Cursor, Connection
from contextlib import contextmanager
from typing import Optional

db_file_name = "groceries.db"
dir_path  = __file__.rsplit("/", maxsplit=1)[0]
path_with_name = f"{dir_path}/{db_file_name}"
print(f"creating db file at path: {path_with_name}")

@contextmanager
def db_conn():
    conn: Optional[Connection] = None

    try:
        conn = sqlite3.connect(path_with_name)
        csr: Cursor = conn.cursor()
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



conn = sqlite3.connect(path_with_name)
cursor = conn.cursor()

query_string = """create table if not exists groceries(
    id text primary key, 
    name text not null,
    price numeric not null
)"""

with db_conn() as csr:
    csr.execute(query_string)