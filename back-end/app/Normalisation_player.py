import os
import json
import pandas as pd

# Chemin vers le dossier contenant les fichiers JSON
json_folder = 'back-end\data\player'

# Liste pour stocker les données
data = []

# Fonction pour extraire les informations d'un fichier JSON
def extract_data_from_json(json_file):
    with open(json_file, 'r') as f:
        player_data = json.load(f)
        
    if player_data["success"] == 1:
        for player in player_data["result"]:
            player_key = player["player_key"]
            player_name = player["player_name"]
            player_country = player["player_country"]
            player_bday = player["player_bday"]
            player_logo = player["player_logo"]

            for stat in player["stats"]:
                row = {
                    "player_key": player_key,
                    "player_name": player_name,
                    "player_country": player_country,
                    "player_bday": player_bday,
                    "player_logo": player_logo,
                    "season": stat["season"],
                    "type": stat["type"],
                    "rank": stat["rank"],
                    "titles": stat["titles"],
                    "matches_won": stat["matches_won"],
                    "matches_lost": stat["matches_lost"],
                    "hard_won": stat["hard_won"],
                    "hard_lost": stat["hard_lost"],
                    "clay_won": stat["clay_won"],
                    "clay_lost": stat["clay_lost"],
                    "grass_won": stat["grass_won"],
                    "grass_lost": stat["grass_lost"]
                }
                data.append(row)

# Lire tous les fichiers JSON dans l'intervalle de 1 à 66526
for i in range(1, 66527):
    file_name = f'player_player={i}.json'
    file_path = os.path.join(json_folder, file_name)
    if os.path.exists(file_path):
        try:
            extract_data_from_json(file_path)
        except Exception as e:
            print(f"Erreur en lisant le fichier {file_name}: {e}")

# Créer un DataFrame à partir des données
df = pd.DataFrame(data)

# Chemin du fichier CSV de sortie
output_csv_path = 'back-end\data\player_csv\player_statistics.csv'

# Créer le répertoire de sortie s'il n'existe pas
os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

# Sauvegarder le DataFrame en un fichier CSV
df.to_csv(output_csv_path, index=False)

print(f"Les données ont été extraites et sauvegardées dans '{output_csv_path}'")
