import requests
import json


def tester_api(url):
    try:
        response = requests.get(url)
        # Vérifie le statut de la réponse
        if response.status_code == 200:
            print("La requête a réussi !")
            return response.json()  # Retourne les données JSON retournées
        else:
            print("La requête a échoué avec le statut :", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Une erreur s'est produite lors de la requête :", e)
        return None

url_api = "https://api.the-odds-api.com/v4/sports/?apiKey=239cb957397fea1034544122b356c4ca"

data = tester_api(url_api)

if data:
    # Enregistre les données dans un fichier JSON
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(data))
    print("Les données ont été enregistrées dans data.json avec succès.")
else:
    print("Impossible de récupérer les données de l'API.")
