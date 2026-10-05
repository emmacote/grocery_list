from flask import Flask, jsonify, request

import sqlite3
from typing import Optional
from . import db_conn

app: Flask = Flask(__name__)


@app.route("/groceries", methods=["GET"])
def get_groceries():

    with db_conn() as csr:
        query = "select id, name, price from groceries"
        res = csr.execute(query)
        groceries = [dict(id=id, name=name, price=price) for id, name, price in res.fetchall()]

    return jsonify(dict(groceries=groceries))


@app.route("/addfood", methods=["POST"])
def add_food():

    new_food: Optional[dict] = request.get_json()
    if new_food is None:
        return jsonify(error="Missing JSON object. Please send one with (id, name, price)"), 400

    required_fields = "id name price".split(" ")
    for required_field in required_fields:
        if required_field not in new_food:
            return jsonify(error="The Submitted JSON object doesn't have all necessary fields. Required: (id, name, price)"), 400

    new_id = new_food["id"]
    new_name = new_food["name"]
    new_price = new_food["price"]

    with db_conn() as csr:
        query = """insert into groceries(id, name, price) values(?, ?, ?)"""
        csr.execute(query, (new_id, new_name, new_price))

    return jsonify(status=f"Food added... ({new_id}, {new_name}, {new_price})")


@app.route("/food/<id>", methods=["DELETE"])
def delete_food(id):
    delete_query = "delete from groceries where id=?"
    with db_conn() as csr:
        csr.execute(delete_query, (id,))

    return jsonify(status=f"Food deleted -- id: {id}")
