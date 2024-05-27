from flask import Blueprint, jsonify
from datetime import datetime
from app.update_data import update_tennis_data
from app.requête_API import store_last_update



api = Blueprint("api", __name__)

@api.route("/update_data")
def update_data():
    # This will fetch data from the API and write it to the CSV file.
    return jsonify({"success": "/update_data successed"})


@api.route("/get_data")
def get_data():
    return jsonify({"success": "/get_data successed"})


@api.route("/get_matches")
def get_matches():
    print("test get matches")
    data = update_tennis_data()
    return jsonify(data)