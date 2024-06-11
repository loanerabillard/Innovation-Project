import requests
from pprint import pprint
import json
import time
from datetime import datetime, timedelta

# Remplacez 'your_account_APIkey' par votre clé API réelle
api_key = "bf8a5d412a8f1b910160b6f1acfe69ab93e86c8ceb5c8c170561affcbbecaadc"

def get_tennis_match(api_key, days_ahead,league_key):
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2024, 6, 8)
    # end_date = start_date + timedelta(days=days_ahead)
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

def get_tennis_players(api_key, key_players):

    for key_player in key_players:
        url = f"https://api.api-tennis.com/tennis/?method=get_players&player_key={key_player}&APIkey={api_key}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Vérifie si la requête a réussi
            data = response.json()
            
            # Enregistrer les données dans un fichier JSON
            register_file_player(key_player, data,"player")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred on {key_player}: {http_err}")
        except Exception as err:
            print(f"An error occurred on {key_player}: {err}")

        # Attendre 10 secondes avant la prochaine requête
        time.sleep(1)





def register_file_sl(date, data,type,league_key):
    file_name = f"{type}es/{type}_date={date},league={league_key}.json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def register_file_odds(date, data,type,league_key):
    file_name = f"{type}/{type}_date={date},league={league_key}.json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def register_file_player(key_player, data,type):
    file_name = f"{type}/{type}_player={key_player}.json"
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

my_list = [  373,   447,   457,  1990,  1813,  2814,  2072,  1972,  2828,
        3224,  2959,   518,  1766,  2169,  1125,  1749,   477,  2389,
        1094,   454,  1097,   512,  1777,  2826,  2850,  2801,  2833,
         513,  2847,  1910,  2841,  1989,  2973,  2172,   435,   517,
        1132,  1906,  1824,  1155,  1803,   465,  1812,   451,   464,
        2806,   593, 33998,  2980,    67,  1951,  1976,  2815,  1151,
        2693,  2076,   393,  2176,  1772,  2384,  1093,  2813,  1901,
         432,  2414,   364,  2812,  1913,  1121,    70,  2981,  2827,
        1770,  3214,  2972,  1980,  1820,  2083,  1129,  1062,   482,
         423,  1775,  1825,  2829,  2996,  2846,  1911,  7011,  2832,
        2382,   207,  2817,  1826,  1105,  2843,  2675,  2820,  1059,
        2171,  1104,  2392,  1072,  9354,   827,   414,   495,   371,
        1810,  1878,   403,  2387,   430,  2991,  1960,  2835,   386,
        9105,  1905,  1787,  2394,   437,   421,  1106,   363,  2178,
        1079,  2849,  1095,  2004,  1192,  2005,   446,   358,  2173,
        1099,  1101,  2842,   566,   590,  2831,  9393,  2903,  1083,
         473,  1895,   505,  2692,  1764,  2810,   211,  1308,  9534,
        8158,  1134,  1434,  1747,   515,   489,   400,  2390,  1958,
        1074,   521,   132,  3007,  3136,  2694,  2807,  1759,   635,
        2174,  1746,   499, 50379,   780,    92,   427,  1796,   455,
        1150,  1148, 28221, 11621, 53774,   627,   415,  1100,   474,
        2834,  2961,   516,  2823,   438,  1136,   396,  1735,  2993,
        2816,   897,   222,   383,  2383,  1833,  3317,  2837,   433,
       55871, 29882,  1141,  3393,  1779,  2022,   501,  2839,  2683,
        2845, 33659, 23885,  1792,  2811,  2838,  2071,  2840,   479,
         426, 10911,  2844,  3706,   157,    91,   453,  2084,  2406,
         115,  8926,  2073,  2689,   388,  2191,   439,  1894,   209,
        1805,  2089,  2393,  1177,   564,  4172,  2467,  2904,   402,
         896,  1783,  1902,  1802, 22722,  2735,  1399,   374,   569,
        1900,  3219,   459,  2177,   527,  2088, 10148,   524,   818,
        3490,   173,  1102, 60468, 11154,   379,  2853,  1146,  1736,
         359,  1818,    81,  6651,   767,  1926,   372,  9532,  2074,
        2805, 37971,   196,  2100,  1823,  1754,  6701,  2802,   412,
        1145, 13091, 34409,  1828,  1794,   507,  1206,  9107,  1068,
         932, 13031,  1251,   717,  1090,  1232,  2167,  2408,  1070,
       40058,   472,   509,  1066,  2002,   463,  2982,  1098,  2998,
        1077,  2919,  1755,  1112,  2978,  1317,   508,  2697,   392,
        1091, 19431, 15346,   136,  1185,  1189,  1154,  8781,   949,
        3915,  1089,   462,   357,  2848,   449,  2910,  2281,  1331,
        1441,   510,1356,494]

# Remplacez 'your_api_key_here' par votre clé API
api_key = 'bf8a5d412a8f1b910160b6f1acfe69ab93e86c8ceb5c8c170561affcbbecaadc'
num_days = 3

# get_tennis_match(api_key, num_days,266)
# get_tennis_odds(api_key,num_days,266)
# get_tennis_match(api_key, num_days,265)
# get_tennis_odds(api_key,num_days,265)
# get_tennis_match(api_key, num_days,272)
# get_tennis_odds(api_key,num_days,272)
get_tennis_players(api_key, my_list)







