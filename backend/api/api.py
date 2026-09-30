from flask import Flask, jsonify, request
from flask.app import Flask

import sqlite3
from sqlite3 import connect, Connection, Cursor
from contextlib import contextmanager
from typing import Optional

app: Flask = Flask(__name__)

@contextmanager
def db_conn():
    conn: Optional[Connection] = None

    try:
        conn = sqlite3.connect("groceries.db")
        csr: Cursor = conn.cursor()
        yield csr
    except:
        print(f"Database connection failed.")
        raise Exception(f"Database connection failed.")
    finally:
        if conn:
            conn.commit()
            conn.close()


@app.route("/groceries", methods=["GET"])
def get_groceries():
    conn = sqlite3.connect("groceries.db")
    csr = conn.cursor()

    with db_conn() as csr:
        query = "select id, name, price from groceries"
        res = csr.execute(query)
        groceries = [dict(id=id, name=name, price=price) for id, name, price in res.fetchall()]
        csr.close()

    return jsonify(dict(groceries=groceries))

@app.route("/addfood", methods=["POST"])
def add_food():
    new_food = request.get_json()
    new_id = new_food["id"]
    new_name = new_food["name"]
    new_price = new_food["price"]

    with db_conn() as csr:
        query = """insert into groceries(id, name, price) values(?, ?, ?)"""
        csr.execute(query, (new_id, new_name, new_price))
        csr.close()
    return "done with adding food"