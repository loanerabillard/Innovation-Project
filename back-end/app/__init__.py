from flask import Flask, send_from_directory
from colorama import Fore, Style
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    CORS(app)

    from .routes import api as api_blueprint
    app.register_blueprint(api_blueprint)

    @app.route('/')
    def serve():
        return send_from_directory(app.static_folder, 'index.html')

    @app.errorhandler(404)
    def not_found(e):
        return send_from_directory(app.static_folder, 'index.html')

    print(Fore.BLUE)
    print("Get matches : http://localhost:5000/get_matches")
    print(Style.RESET_ALL)
    return app
