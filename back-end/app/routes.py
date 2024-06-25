from flask import Blueprint, jsonify, send_from_directory
from app.update_data import update_tennis_data
from app.requête_API import store_last_update
from flask import request
import os

api = Blueprint("api", __name__)

@api.route('/update_data')
def update_data():
    return jsonify({"success": "/update_data successed"})

@api.route('/get_data')
def get_data():
    return jsonify({"success": "/get_data successed"})

@api.route('/get_matches')
def get_matches():
    num_matches = request.args.get('num_matches', default=20, type=int)
    print(f"Requested number of matches: {num_matches}")
    data = update_tennis_data(num_matches)
    print('/get_matches fini')
    return jsonify(data)

# Serve frontend
@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("app/static/" + path):
        return send_from_directory('static', path)
    else:
        return send_from_directory('static', 'index.html')
