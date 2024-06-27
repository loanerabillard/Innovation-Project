#donne moi les imports de ce fichier
from datetime import datetime
from app.requête_API import requête, store_last_update
from app.Algo import get_matches_dicts, incoming_games_ids, algo_répartition, get_best_matches, register_data
from app.Normalisation import Normalisation
from app.Normalisation2 import Normalisation2
from app.Response import get_json_data
from app.tools import timeit

@timeit
def update_tennis_data(num_matches=10, test_mode=False):

    # Read the last update date from the file
    with open('last_update.txt', 'r') as file:
        try:
            last_update = datetime.strptime(file.read(), "%d-%m-%y").strftime("%d-%m-%y")
        except:
            last_update = None

    # Get the current date
    now = datetime.now().strftime("%d-%m-%y")

    # Compare the dates
    if test_mode:
        return get_api_data(num_matches, now, test_mode)

    if last_update is None:
        print('=> last_update is None')
        return get_api_data(num_matches, now)
    if (last_update != now):
        print(last_update)
        print(now)
        print('=> last_update is a different day')
        return get_api_data(num_matches, now)
    
  
    print('=> Data created for the current day')
    return get_json_data(f"responses/matches_{now}.json")

@timeit
def get_api_data(num_matches, now, test_mode=False):
    if not test_mode:
        store_last_update()
        requête()
        Normalisation()
        Normalisation2()
    data1 = get_best_matches(get_matches_dicts(incoming_games_ids()), num_matches, use_surface_wr=True)
    data = algo_répartition(data1, num_matches)
    register_data(data, now)
    return get_json_data(f"responses/matches_{now}.json")