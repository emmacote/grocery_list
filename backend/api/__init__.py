import sqlite3

# TODO: This path setup kind of sucks.
db_file_name = "groceries.db"
dir_path  = __file__.rsplit("/", maxsplit=1)[0]
path_with_name = f"{dir_path}/{db_file_name}"
print(f"creating db file at path: {path_with_name}")
conn = sqlite3.connect(path_with_name)
cursor = conn.cursor()

query_string = """create table if not exists groceries(
    id text primary key, 
    name text not null,
    price numeric not null
)"""

cursor.execute(query_string)
cursor.close()
conn.close()