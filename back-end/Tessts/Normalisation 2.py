import os
import json
import pandas as pd

def Normalisation():
    input_folder = './matches'  # dossier contenant les fichiers JSON
    output_folder = './matches_csv'  # dossier où les fichiers CSV seront enregistrés
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create empty dataframes for sets and points
    sets_df = pd.DataFrame(columns=['match_id', 'set_number', 'number_game', 'player_served', 'serve_winner', 'serve_lost', 'score', 'point_ids'])
    points_df = pd.DataFrame(columns=['point_id', 'number_point', 'score', 'break_point', 'set_point', 'match_point'])

    # Lists to hold data temporarily
    sets_list = []
    points_list = []
    
    # Counter for unique point IDs
    point_id_counter = 1

    # Iterate over all JSON files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            with open(os.path.join(input_folder, filename), 'r') as file:
                data = json.load(file)
                
                if 'result' in data:
                    # Extract match_id, set_info, and point_ids from the data
                    match_id = data['result'][0]['event_key']
                    for set_info in data['result'][0]['pointbypoint']:
                        if 'points' in set_info:
                            point_ids = []
                            for point in set_info['points']:
                                point_id = point_id_counter
                                point_id_counter += 1
                                point_ids.append(point_id)
                                
                                points_list.append({
                                    'point_id': point_id, 
                                    'number_point': point['number_point'], 
                                    'score': point['score'], 
                                    'break_point': point['break_point'], 
                                    'set_point': point['set_point'], 
                                    'match_point': point['match_point']})

                            sets_list.append({
                                'match_id': match_id, 
                                'set_number': set_info['set_number'], 
                                'number_game': set_info['number_game'], 
                                'player_served': set_info['player_served'], 
                                'serve_winner': set_info['serve_winner'], 
                                'serve_lost': set_info['serve_lost'], 
                                'score': set_info['score'], 
                                'point_ids': point_ids})

    # Convert lists to DataFrames
    sets_df = pd.DataFrame(sets_list)
    points_df = pd.DataFrame(points_list)

    # Save the dataframes to CSV files
    sets_df.to_csv(os.path.join(output_folder, 'sets.csv'), index=False)
    points_df.to_csv(os.path.join(output_folder, 'points.csv'), index=False)

# Appel de la fonction pour exécuter le code
Normalisation()
