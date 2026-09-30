import sqlite3

conn = sqlite3.connect("groceries.db")
cursor = conn.cursor()

query_string = """create table if not exists groceries(
    id text primary key, 
    name text not null,
    price numeric not null
)"""

cursor.execute(query_string)
cursor.close()
conn.close()