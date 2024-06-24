import json

def get_json_data(file_path):
    with open(f"data/{file_path}", 'r') as file:
        data = json.load(file)
    return data

