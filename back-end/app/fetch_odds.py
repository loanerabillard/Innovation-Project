import json

API_KEY = None

with open("config.json", "r") as config_file:
    config = json.load(config_file)
    API_KEY = config.get("API_KEY")

def fetch_odds():
    ...