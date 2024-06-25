#donne moi les imports de ce fichier
from datetime import datetime
from app.requête_API import requête, store_last_update
from app.Algo import RESPONSE, incoming_games, algo_répartition, RESPONSE2, register_data
from app.Normalisation import Normalisation
from app.Normalisation2 import Normalisation2
from app.Response import get_json_data

def update_tennis_data(num_matches=10):
    # Read the last update date from the file
    with open('last_update.txt', 'r') as file:
        try:
            last_update = datetime.strptime(file.read(), "%d-%m-%y").strftime("%d-%m-%y")
        except:
            last_update = None

    # Get the current date
    now = datetime.now().strftime("%d-%m-%y")

    # Compare the dates

    if last_update is None:
        print('last_update is None')
        return get_api_data(num_matches, now)
    if (last_update != now):
        print(last_update)
        print(now)
        print('last_update is a different day')
        return get_api_data(num_matches, now)
    
    # data1 = RESPONSE2(RESPONSE(incoming_games()), num_matches)
    # data = algo_répartition(data1, num_matches)
    # register_data(data)
    # data1 = RESPONSE2(RESPONSE(incoming_games()), num_matches)
    # data = algo_répartition(data1, num_matches)
    # register_data(data, now)
    print('Data created for the current day')
    return get_json_data(f"responses/matches_{now}.json")


def get_api_data(num_matches, now):
    store_last_update()
    requête()
    Normalisation()
    Normalisation2()
    data1 = RESPONSE2(RESPONSE(incoming_games()), num_matches)
    data = algo_répartition(data1, num_matches)
    register_data(data, now)
    return get_json_data(f"responses/matches_{now}.json")