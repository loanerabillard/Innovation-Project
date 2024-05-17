import requests
import json

def get_season():
    url = "https://v1.hockey.api-sports.io//seasons"
    payload = {}
    headers = {
        'x-rapidapi-key': '181b008f0f91004c17435e30ad18299b',
        'x-rapidapi-host': 'v1.hockey.api-sports.io'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    seasons = data['response']
    return seasons

def get_league(seasons):
    all_matches = []
    for season in seasons:
        url = f"https://v1.hockey.api-sports.io//leagues?season={season}"
        payload = {}
        headers = {
            'x-rapidapi-key': '181b008f0f91004c17435e30ad18299b',
            'x-rapidapi-host': 'v1.hockey.api-sports.io'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        leagues = data['response']
        for league in leagues:
            league_id = league['id']
            league_name = league['name']
            matches = get_matches_for_league(league_id, season)
            all_matches.append({
                'league_id': league_id,
                'league_name': league_name,
                'matches': matches
            })
    return all_matches

def get_matches_for_league(league_id, season):
    url = f"https://v1.hockey.api-sports.io//matches?league={league_id}&season={season}"
    payload = {}
    headers = {
        'x-rapidapi-key': '181b008f0f91004c17435e30ad18299b',
        'x-rapidapi-host': 'v1.hockey.api-sports.io'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    matches = data['response']
    return matches

# Example usage:
seasons = get_season()
all_league_matches = get_league(seasons)
print(all_league_matches)
