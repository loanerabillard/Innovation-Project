from flask import Blueprint, jsonify
from app.Algo import RESPONSE, incoming_games, Algo
from app.Normalisation import Normalisation
from app.requête_API import requête

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
    Normalisation()
    data = RESPONSE(incoming_games())
    return jsonify(data)