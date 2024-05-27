#donne moi les imports de ce fichier
from datetime import datetime
from app.requête_API import requête, store_last_update
from app.Algo import RESPONSE, incoming_games
from app.Normalisation import Normalisation

def update_tennis_data():
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
        data = RESPONSE(incoming_games())
    else:
        # If the dates are equal, execute only RESPONSE(incoming_games())
        data = RESPONSE(incoming_games())
    return data