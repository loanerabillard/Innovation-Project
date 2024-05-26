from requête_API import get_tennis_match,get_tennis_odds
from Normalisation import Normalisation
from Algo import RESPONSE,incoming_games, Algo

def update_data():

    api_key = '655be1d40fee55b7f780c811244b2375646a0f4acd0a5d935d8a94b10600026e'
    num_days = 3
    print(0)
    get_tennis_odds(api_key,num_days)
    print("1")
    get_tennis_match(api_key, num_days)
    print("2")
    Normalisation()
    print("3")

    return RESPONSE(incoming_games())

