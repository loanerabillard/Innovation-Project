from flask import Flask
from colorama import Fore, Style
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import api as api_blueprint
    app.register_blueprint(api_blueprint)

    print(Fore.BLUE)
    # print("Update data : http://localhost:5000/update_data")
    print("Get matches : http://localhost:5000/get_matches")
    # print("Get Data : http://localhost:5000/get_data")
    print(Style.RESET_ALL)
    return app
