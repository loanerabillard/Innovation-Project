import os
import json
import pandas as pd
import csv

def Normalisation():

    def extract_data_to_dataframe(json_data):
        events = []
        scores = []
        
        if 'result' in json_data:
            for event in json_data['result']:
                event_data = {
                    "event_key": event["event_key"],
                    "event_date": event["event_date"],
                    "event_time": event["event_time"],
                    "event_first_player": event["event_first_player"],
                    "first_player_key": event["first_player_key"],
                    "event_first_player_logo": event["event_first_player_logo"],
                    "event_second_player": event["event_second_player"],
                    "second_player_key": event["second_player_key"],
                    "event_second_player_logo": event["event_second_player_logo"],
                    "event_final_result": event["event_final_result"],
                    "event_game_result": event["event_game_result"],
                    "event_winner": event["event_winner"],
                    "event_status": event["event_status"],
                    "event_type_type": event["event_type_type"],
                    "tournament_name": event["tournament_name"],
                    "tournament_key": event["tournament_key"],
                    "tournament_round": event["tournament_round"],
                    "tournament_season": event["tournament_season"],
                    "event_live": event["event_live"]
                }
                events.append(event_data)
                
                for score in event["scores"]:
                    score_data = {
                        "event_key": event["event_key"],
                        "score_first": score["score_first"],
                        "score_second": score["score_second"],
                        "score_set": score["score_set"]
                    }
                    scores.append(score_data)
        
        df_events = pd.DataFrame(events)
        df_scores = pd.DataFrame(scores)
        
        return df_events, df_scores

    def Norm_matches(input_folder, output_folder):
        all_events = []
        all_scores = []
        
        for filename in os.listdir(input_folder):
            if filename.endswith('.json'):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r') as file:
                    json_data = json.load(file)
                    if 'result' in json_data:
                        df_events, df_scores = extract_data_to_dataframe(json_data)
                        all_events.append(df_events)
                        all_scores.append(df_scores)
        
        if all_events:
            combined_events = pd.concat(all_events, ignore_index=True)
            combined_scores = pd.concat(all_scores, ignore_index=True)
            
            combined_events.to_csv(os.path.join(output_folder, 'events.csv'), index=False)
            combined_scores.to_csv(os.path.join(output_folder, 'scores.csv'), index=False)



    def Norm_odds(json_files, output_csv_path):
        with open(output_csv_path, 'w', newline='') as csvfile:
            fieldnames = ['id_match', 'bookmaker', 'cote_Home', 'cote_Away']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for json_file_path in json_files:
                with open(json_file_path) as json_file:
                    json_data = json.load(json_file)
                    if 'result' in json_data:
                        for id_match, match_data in json_data['result'].items():
                            home_odds = match_data.get('Home/Away', {}).get('Home', {})
                            away_odds = match_data.get('Home/Away', {}).get('Away', {})
                            for bookmaker, home_odd in home_odds.items():
                                away_odd = away_odds.get(bookmaker)
                                writer.writerow({'id_match': id_match, 'bookmaker': bookmaker, 'cote_Home': home_odd, 'cote_Away': away_odd})



    folder_path = './data/odds'
    csv_folder_path ="./data/odds_csv/odds.csv"
    json_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.json')]
    # Utilisation de la fonction avec le chemin du dossier JSON en entrée et le nom du fichier CSV en sortie
    Norm_odds(json_files, csv_folder_path)






    # # Utilisation de la fonction Match
    input_folder = 'data/matches'  # dossier contenant les fichiers JSON
    output_folder = 'data/matches_csv'  # dossier où les fichiers CSV seront enregistrés
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    Norm_matches(input_folder, output_folder)
