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
        last_update = datetime.strptime(file.read(), '%Y-%m-%d %H:%M:%S.%f')

    # Get the current date
    now = datetime.now()
    print(last_update.date(), now.date())
    # Compare the dates
    if last_update.date() != now.date():
        # If the dates are different, execute requete(), Normalisation() and RESPONSE(incoming_games())
        store_last_update()
        requête()
        Normalisation()
        Normalisation2()
        data1 = RESPONSE2(RESPONSE(incoming_games()), num_matches)
        data = algo_répartition(data1, num_matches)
        register_data(data)
        return get_json_data("matches.json")
    else:
        return get_json_data("matches.json")