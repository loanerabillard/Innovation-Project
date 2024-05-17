from flask import Blueprint, jsonify


api = Blueprint("api", __name__)

@api.route("/update_data")
def update_data():
    # This will fetch data from the API and write it to the CSV file.
    return jsonify({"success": "/update_data successed"})


@api.route("/get_data")
def get_data():
    return jsonify({"success": "/get_data successed"})