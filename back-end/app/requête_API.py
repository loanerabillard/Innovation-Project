import requests
from pprint import pprint
import json
import time
from datetime import datetime, timedelta

def requête():
    # Remplacez 'your_account_APIkey' par votre clé API réelle
    api_key = "655be1d40fee55b7f780c811244b2375646a0f4acd0a5d935d8a94b10600026e"

    def get_tennis_match(api_key, days_ahead,league_key):
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=days_ahead)
        current_date = start_date

        while current_date <= end_date:
            date_str = current_date.strftime('%Y-%m-%d')
            url = f"https://api.api-tennis.com/tennis/?method=get_fixtures&date_start={date_str}&date_stop={date_str}&event_type_key={league_key}&APIkey={api_key}"
            
            try:
                response = requests.get(url)
                response.raise_for_status()  # Vérifie si la requête a réussi
                data = response.json()
                
                # Enregistrer les données dans un fichier JSON
                register_file_sl(date_str, data, "match",league_key)

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred on {date_str}: {http_err}")
            except Exception as err:
                print(f"An error occurred on {date_str}: {err}")

            # Attendre 10 secondes avant la prochaine requête
            time.sleep(10)
            current_date += timedelta(days=1)




    def get_tennis_odds(api_key, num_days,league_key):
        start_date = datetime.now().date()
        end_date = start_date + timedelta(days=num_days)
        current_date = start_date

        while current_date <= end_date:
            date_str = current_date.strftime('%Y-%m-%d')
            url = f"https://api.api-tennis.com/tennis/?method=get_odds&date_start={date_str}&date_stop={date_str}&event_type_key={league_key}&APIkey={api_key}"
            
            try:
                response = requests.get(url)
                response.raise_for_status()  # Vérifie si la requête a réussi
                data = response.json()
                
                # Enregistrer les données dans un fichier JSON
                register_file_odds(date_str, data,"odds",league_key)

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred on {date_str}: {http_err}")
            except Exception as err:
                print(f"An error occurred on {date_str}: {err}")

            # Attendre 10 secondes avant la prochaine requête
            time.sleep(10)
            current_date += timedelta(days=1)


    def register_file_sl(date, data,type,league_key):
        file_name = f"data/{type}es/{type}_date={date},league={league_key}.json"
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def register_file_odds(date, data,type,league_key):
        file_name = f"data/{type}/{type}_date={date},league={league_key}.json"
        with open(file_name, 'w') as json_file:
            json.dump(data, json_file, indent=4)



    # Remplacez 'your_api_key_here' par votre clé API
    api_key = '655be1d40fee55b7f780c811244b2375646a0f4acd0a5d935d8a94b10600026e'
    num_days = 3

    get_tennis_match(api_key, num_days,266)
    get_tennis_odds(api_key,num_days,266)
    get_tennis_match(api_key, num_days,265)
    get_tennis_odds(api_key,num_days,265)

def store_last_update():
    with open('last_update.txt', 'w') as file:
        file.write(str(datetime.today()))





