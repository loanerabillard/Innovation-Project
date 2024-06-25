import pandas as pd
import ast
import numpy as np
from datetime import datetime

def load_data():
    events_df = pd.read_csv("back-end\data\matches_csv\events.csv")
    scores_df = pd.read_csv("back-end\data\matches_csv\scores.csv")
    points_df = pd.read_csv("back-end\data\matches_csv\points.csv")
    sets_df = pd.read_csv("back-end\data\matches_csv\sets.csv")
    player_df = pd.read_csv('back-end\data\player_csv\player_statistics.csv')
    return events_df, scores_df, points_df, sets_df, player_df

def process_sets_df(sets_df, points_df):
    sets_df['point_ids'] = sets_df['point_ids'].apply(ast.literal_eval)
    unpacked_sets_df = sets_df.explode('point_ids')
    merged_df = unpacked_sets_df.merge(points_df, left_on='point_ids', right_on='point_id', how='left')
    merged_df.drop(columns=['point_ids'], inplace=True)
    merged_df.rename(columns={'score_x': 'score_sets', 'score_y': 'score_points'}, inplace=True)
    return merged_df

def process_scores_df(merged_df, scores_df):
    merged_df['set_number'] = merged_df['set_number'].str.split().str[-1].astype(int)
    merged_scores_df = pd.merge(merged_df, scores_df, left_on=['match_id', 'set_number'], right_on=['event_key', 'score_set'], how='left')
    merged_scores_df.drop(['event_key', 'score_set'], axis=1, inplace=True)
    return merged_scores_df

def merge_with_events(merged_scores_df, events_df):
    final_df = pd.merge(merged_scores_df, events_df, left_on='match_id', right_on='event_key', how='left')
    final_df.drop('event_key', axis=1, inplace=True)
    return final_df

def clean_data(final_df):
    df = final_df.copy()

    df[['break_point', 'set_point', 'match_point']] = df[['break_point', 'set_point', 'match_point']].applymap(lambda x: 1 if x == 'First Play' else 0 if pd.isna(x) else x)
    df['serve_lost'].fillna(value="N/A", inplace=True)
    df = df[~df['event_status'].isin(['Cancelled', '1', 'Set 1', 'Set 2', 'Set 3', 'Set 4'])]
    df['tournament_round'].fillna('Unknown', inplace=True)
    df.dropna(subset=['event_status'], inplace=True)
    df.drop(columns=['event_first_player_logo', 'event_second_player_logo'], inplace=True)
    df['score_first'].fillna("N/A", inplace=True)
    df['score_second'].fillna("N/A", inplace=True)

    # Replace player names for specific columns
    for index, row in df.iterrows():
        if row['player_served'] == 'First Player':
            df.at[index, 'player_served'] = row['event_first_player']
        elif row['player_served'] == 'Second Player':
            df.at[index, 'player_served'] = row['event_second_player']
        
        if row['serve_winner'] == 'First Player':
            df.at[index, 'serve_winner'] = row['event_first_player']
        elif row['serve_winner'] == 'Second Player':
            df.at[index, 'serve_winner'] = row['event_second_player']
        
        if row['serve_lost'] == 'First Player':
            df.at[index, 'serve_lost'] = row['event_first_player']
        elif row['serve_lost'] == 'Second Player':
            df.at[index, 'serve_lost'] = row['event_second_player']
        
        if row['event_winner'] == 'First Player':
            df.at[index, 'event_winner'] = row['event_first_player']
        elif row['event_winner'] == 'Second Player':
            df.at[index, 'event_winner'] = row['event_second_player']

    # Map tournament names to surfaces
    surface_mapping = {
        'US Open': 'hard', 'Adelaide': 'hard', 'Auckland': 'hard', 'Hobart': 'hard', 'Australian Open': 'hard',
        'Lyon': 'clay', 'Hua Hin': 'hard', 'Abu Dhabi': 'hard', 'Cordoba': 'clay', 'Rotterdam': 'hard',
        'Doha': 'hard', 'Dubai': 'hard', 'Merida': 'hard', 'WTA Austin': 'hard', 'ATP Dubai': 'hard',
        'ATP Santiago': 'clay', 'WTA Indian Wells': 'hard', 'ATP Indian Wells': 'hard', 'WTA Miami': 'hard',
        'ATP Miami': 'hard', 'ATP Estoril': 'clay', 'WTA Bogota': 'clay', 'ATP Marrakech': 'clay',
        'WTA Charleston': 'clay', 'ATP Houston': 'clay', 'ATP Monte Carlo': 'clay',
        'WTA Billie Jean King Cup - Group I': 'various', 'WTA Billie Jean King Cup - World Group': 'various',
        'WTA Stuttgart': 'clay', 'ATP Munich': 'clay', 'ATP Barcelona': 'clay', 'ATP Banja Luka': 'clay',
        'WTA Madrid': 'clay', 'ATP Madrid': 'clay', 'WTA Rome': 'clay', 'ATP Rome': 'clay', 'WTA Rabat': 'clay',
        'ATP Lyon': 'clay', 'ATP Geneva': 'clay', 'WTA Strasbourg': 'clay', 'ATP Hertogenbosch': 'grass',
        'WTA Hertogenbosch': 'grass', 'WTA Nottingham': 'grass', 'WTA Billie Jean King Cup - Group III': 'various',
        'ATP Davis Cup - Group III': 'various', 'ATP Stuttgart': 'grass', 'WTA Berlin': 'grass', 'ATP Halle': 'grass',
        'WTA Birmingham': 'grass', 'ATP Eastbourne': 'grass', 'ATP Mallorca': 'grass', 'WTA Eastbourne': 'grass',
        'ATP Wimbledon': 'grass', 'WTA Bad Homburg': 'grass', 'WTA Wimbledon': 'grass', 'ATP Gstaad': 'clay',
        'WTA Palermo': 'clay', 'WTA Budapest': 'clay', 'ATP Newport': 'grass', 'ATP Bastad': 'clay',
        'WTA Warsaw': 'clay', 'ATP Hamburg': 'clay', 'WTA Hamburg': 'clay', 'ATP Atlanta': 'hard',
        'WTA Billie Jean King Cup - Group II': 'various', 'WTA Washington': 'hard', 'WTA Livesport Prague Open': 'hard',
        'ATP Kitzbuhel': 'clay', 'ATP Washington': 'hard', 'ATP Davis Cup - Group IV': 'various', 'WTA Montreal': 'hard',
        'ATP Toronto': 'hard', 'ATP Cincinnati': 'hard', 'WTA Cincinnati': 'hard', 'WTA Cleveland': 'hard',
        'ATP Winston-Salem': 'hard', 'WTA US Open': 'hard', 'ATP US Open': 'hard', 'WTA Osaka': 'hard',
        'WTA San Diego': 'hard', 'ATP Davis Cup - World Group': 'various', 'ATP Davis Cup - World Group I': 'various',
        'WTA Guadalajara': 'hard', 'ATP Davis Cup - World Group II': 'various', 'ATP Chengdu': 'hard',
        'WTA Ningbo': 'hard', 'ATP Zhuhai': 'hard', 'WTA Tokyo': 'hard', 'ATP Astana': 'hard',
        'ATP Asian Games': 'various', 'WTA Beijing': 'hard', 'ATP Beijing': 'hard', 'ATP Shanghai': 'hard',
        'WTA Zhengzhou': 'hard', 'WTA Seoul': 'hard', 'WTA Hong Kong': 'hard', 'ATP Tokyo': 'hard',
        'WTA Cluj-Napoca': 'hard', 'ATP Antwerp': 'hard', 'WTA Monastir': 'hard',
        'ATP Stockholm': 'hard', 'WTA Nanchang': 'hard', 'ATP Basel': 'hard', 'Zhuhai': 'hard',
        'ATP Vienna': 'hard', 'WTA Finals - Cancun': 'hard', 'ATP Paris': 'hard',
        'ATP Metz': 'hard', 'ATP Sofia': 'hard', 'ATP Finals - Turin': 'hard',
        'ATP Next Gen Finals - Jeddah': 'hard', 'WTA Auckland': 'hard', 'ATP United Cup': 'various',
        'WTA United Cup': 'various', 'ATP Brisbane': 'hard', 'WTA Brisbane': 'hard', 'ATP Hong Kong': 'hard',
        'WTA Hobart': 'hard', 'ATP Adelaide': 'hard', 'WTA Adelaide': 'hard', 'ATP Australian Open': 'hard',
        'WTA Australian Open': 'hard', 'ATP Auckland': 'hard', 'WTA Hua Hin': 'hard', 'ATP Montpellier': 'hard ',
        'WTA Linz': 'hard', 'ATP Cordoba': 'clay', 'WTA Abu Dhabi': 'hard', 'ATP Dallas': 'hard',
        'WTA Doha': 'hard', 'ATP Marseille': 'hard', 'ATP Delray Beach': 'hard', 'ATP Buenos Aires': 'clay',
        'ATP Rotterdam': 'hard', 'WTA Dubai': 'hard', 'ATP Rio de Janeiro': 'clay', 'ATP Doha': 'hard',
        'ATP Los Cabos': 'hard', 'ATP Acapulco': 'hard', 'WTA Rouen': 'hard', 'ATP Bucharest': 'clay',
        'WTA Bogota': 'clay', 'Australian Open': 'hard', 'WTA Charleston': 'clay', 'ATP Estoril': 'clay',
        'WTA French Open': 'clay', 'ATP French Open': 'clay'
    }

    df['surface'] = df['tournament_name'].map(surface_mapping)
    return df

def remove_decimal_zero(value):
    if pd.isna(value):  # Laisser NaN tel quel
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value

def calculate_age(birthdate):
    if pd.isna(birthdate):
        return np.nan
    birthdate = datetime.strptime(birthdate, '%d.%m.%Y')
    today = datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

def process_player_df(player_df):
    cols_to_clean = ["season", "rank", "titles", "matches_won", "matches_lost", "hard_won", "hard_lost", "clay_won", "clay_lost", "grass_won", "grass_lost"]

    for col in cols_to_clean:
        player_df[col] = player_df[col].apply(remove_decimal_zero)

    stat = player_df.groupby('player_key').agg({
        'player_name': 'first',
        'rank': 'min',
        'player_bday': 'first',
        'titles': 'sum',
        'matches_won' : 'sum',
        'hard_won': 'sum',
        'clay_won': 'sum',
        'grass_won': 'sum'
    }).reset_index()

    stat['age'] = stat['player_bday'].apply(calculate_age)

    stat = stat.rename(columns={
        'player_name': 'Nom joueur',
        'rank': 'Rang',
        'titles': 'Nombre titres total',
        'matches_won' : 'Victoire totale',
        'hard_won': 'Victoire Hard',
        'clay_won': 'Victoire Clay',
        'grass_won': 'Victoire Grass',
        'age': 'Age'
    })

    stat['% victoire général'] = (player_df['matches_won'] / (player_df['matches_won'] + player_df['matches_lost'])) * 100

    stat['% victoire hard'] = (player_df['hard_won'] / (player_df['hard_won'] + player_df['hard_lost'])).fillna(0) * 100
    stat['% victoire clay'] = (player_df['clay_won'] / (player_df['clay_won'] + player_df['clay_lost'])).fillna(0) * 100
    stat['% victoire grass'] = (player_df['grass_won'] / (player_df['grass_won'] + player_df['grass_lost'])).fillna(0) * 100

    top_100_mask = player_df['rank'] < 100
    player_top100_victories = player_df[top_100_mask].groupby('player_key')['matches_won'].sum()

    stat['matches_won_top100'] = 0

    valid_player_keys = player_top100_victories.index.intersection(stat.index)
    stat.loc[valid_player_keys, 'matches_won_top100'] = player_top100_victories.loc[valid_player_keys].values

    stat['% victoire contre top 100'] = (stat['matches_won_top100'] / stat['Victoire totale']).fillna(0) * 100

    return stat


def calculer_stats_joueur(nom_joueur, df_match):
    # Sélectionner une seule ligne par match en utilisant match_id
    joueur_matches_unique = df_match.drop_duplicates(subset='match_id', keep='first')
    
    # Filtrer les matchs où le joueur est impliqué comme joueur ou adversaire
    joueur_matches = joueur_matches_unique[(joueur_matches_unique['event_first_player'] == nom_joueur) | 
                                           (joueur_matches_unique['event_second_player'] == nom_joueur)]
    
    # Initialiser une liste pour stocker les statistiques par adversaire
    joueur_stats_list = []
    
    # Liste de tous les adversaires uniques
    adversaires = set(joueur_matches['event_first_player'].unique()).union(set(joueur_matches['event_second_player'].unique()))
    adversaires.discard(nom_joueur)  # Retirer le joueur lui-même de la liste des adversaires

    # Pour chaque adversaire
    for adversaire in adversaires:
        # Filtrer les matchs entre le joueur et cet adversaire
        contre_adversaire = joueur_matches[(joueur_matches['event_first_player'] == adversaire) | 
                                           (joueur_matches['event_second_player'] == adversaire)]
        
        # Nombre total de rencontres entre le joueur et cet adversaire
        nb_rencontres = contre_adversaire.shape[0]
        
        # Nombre de victoires du joueur contre cet adversaire
        nb_victoires = contre_adversaire[contre_adversaire['event_winner'] == nom_joueur].shape[0]
        
        # Calcul du pourcentage de victoire général
        pourcentage_victoire = (nb_victoires / nb_rencontres) * 100 if nb_rencontres > 0 else 0
        
        # Initialiser un dictionnaire pour les statistiques de cet adversaire
        adversaire_stats = {
            'Joueur': nom_joueur,
            'Adversaire': adversaire,
            'Nombre de rencontres': nb_rencontres,
            'Nombre de victoires': nb_victoires,
            '% Victoire': pourcentage_victoire,
            'Nombre de rencontres (hard)': 0,
            'Nombre de victoires (hard)': 0,
            '% Victoire (hard)': 0.0,
            'Nombre de rencontres (clay)': 0,
            'Nombre de victoires (clay)': 0,
            '% Victoire (clay)': 0.0,
            'Nombre de rencontres (grass)': 0,
            'Nombre de victoires (grass)': 0,
            '% Victoire (grass)': 0.0,
            'Nombre de rencontres (various)': 0,
            'Nombre de victoires (various)': 0,
            '% Victoire (various)': 0.0
        }
        
        # Liste des surfaces à considérer
        surfaces = ['hard', 'clay', 'grass', 'various']
        
        # Pour chaque surface, calculer les statistiques si disponibles dans les matchs
        for surface in surfaces:
            matches_surface = contre_adversaire[contre_adversaire['surface'] == surface]
            nb_rencontres_surface = matches_surface.shape[0]
            nb_victoires_surface = matches_surface[matches_surface['event_winner'] == nom_joueur].shape[0]
            pourcentage_victoire_surface = (nb_victoires_surface / nb_rencontres_surface) * 100 if nb_rencontres_surface > 0 else 0
            
            # Ajouter les statistiques par surface au dictionnaire
            adversaire_stats[f'Nombre de rencontres ({surface})'] = nb_rencontres_surface
            adversaire_stats[f'Nombre de victoires ({surface})'] = nb_victoires_surface
            adversaire_stats[f'% Victoire ({surface})'] = pourcentage_victoire_surface
        
        # Ajouter les statistiques de cet adversaire à la liste des statistiques du joueur
        joueur_stats_list.append(adversaire_stats)
    
    # Créer un DataFrame à partir de la liste des statistiques par adversaire
    joueur_stats = pd.DataFrame(joueur_stats_list)
    
    # Trier les statistiques par pourcentage de victoire décroissant
    joueur_stats = joueur_stats.sort_values(by='% Victoire', ascending=False)
    
    return joueur_stats

def calculate_win_probability(player1, player2, surface, merged_df, stat):
    # Conversion de la surface en minuscule pour correspondre aux colonnes du DataFrame
    surface = str(surface).lower()

    # Récupération des statistiques globales des joueurs
    player1_stats = stat[stat['Joueur'] == player1].iloc[0]
    player2_stats = stat[stat['Joueur'] == player2].iloc[0]

    # Calcul du score basé sur les statistiques globales
    score1 = (player1_stats['Rang'] + player1_stats['Nombre titres total'] +
              player1_stats['Victoire totale'] + player1_stats[f'Victoire {surface.capitalize()}'] +
              player1_stats['Age'] + player1_stats['% victoire général'] +
              player1_stats[f'% victoire {surface}'] + player1_stats['matches_won_top100'] +
              player1_stats['% victoire contre top 100'])

    score2 = (player2_stats['Rang'] + player2_stats['Nombre titres total'] +
              player2_stats['Victoire totale'] + player2_stats[f'Victoire {surface.capitalize()}'] +
              player2_stats['Age'] + player2_stats['% victoire général'] +
              player2_stats[f'% victoire {surface}'] + player2_stats['matches_won_top100'] +
              player2_stats['% victoire contre top 100'])

    # Ajustement si les joueurs se sont déjà rencontrés
    previous_matches = merged_df[(merged_df['Joueur'] == player1) & (merged_df['Adversaire'] == player2)]
    if not previous_matches.empty:
        previous_match = previous_matches.iloc[0]
        score1 += (previous_match['Nombre de rencontres'] + previous_match['Nombre de victoires'] +
                   previous_match[f'% Victoire ({surface})'])
        score2 += (previous_match['Nombre de rencontres'] + previous_match['Nombre de victoires'] +
                   previous_match[f'% Victoire ({surface})'])

    # Calcul des probabilités
    total_score = score1 + score2
    win_prob_player1 = score1 / total_score * 100
    win_prob_player2 = score2 / total_score * 100

    return win_prob_player1, win_prob_player2


def main():
    events_df, scores_df, points_df, sets_df, player_df = load_data()
    
    merged_df = process_sets_df(sets_df, points_df)
    merged_scores_df = process_scores_df(merged_df, scores_df)
    final_df = merge_with_events(merged_scores_df, events_df)
    cleaned_df = clean_data(final_df)
    
    stat = process_player_df(player_df)
    
    tous_les_joueurs = set(cleaned_df['event_first_player'].unique()).union(set(cleaned_df['event_second_player'].unique()))
    stats_globales = {}
    
    for joueur in tous_les_joueurs:
        stats_joueur = calculer_stats_joueur(joueur, cleaned_df)
        stats_globales[joueur] = stats_joueur
    
    stats_globales_df = pd.DataFrame()
    
    for joueur, stats_joueur in stats_globales.items():
        stats_joueur['Joueur'] = joueur
        stats_globales_df = pd.concat([stats_globales_df, stats_joueur], ignore_index=True)
    
    stat = stat.rename(columns={'Nom joueur': 'Joueur'})
    stat.dropna(subset=['Rang'], inplace=True)
    stat.dropna(subset=['% victoire général'], inplace=True)
    
    merged_df = pd.merge(stats_globales_df, stat, on='Joueur', how='left')
    
    merged_df.fillna({
        'Adversaire': 'Aucun',
        'Nombre de rencontres': 0,
        'Nombre de victoires': 0,
        '% Victoire': 0.0,
        'Nombre de rencontres (hard)': 0,
        'Nombre de victoires (hard)': 0,
        '% Victoire (hard)': 0.0,
        'Nombre de rencontres (clay)': 0,
        'Nombre de victoires (clay)': 0,
        '% Victoire (clay)': 0.0,
        'Nombre de rencontres (grass)': 0,
        'Nombre de victoires (grass)': 0,
        '% Victoire (grass)': 0.0
    }, inplace=True)
    
    merged_df.dropna(subset=['Rang'], inplace=True)
    
    output_csv_path = 'back-end\data\player_csv\pourcentage_victoire.csv'

    merged_df.to_csv(output_csv_path, index=False)

    # # Appel de calculate_win_probability pour chaque paire de joueurs avec la surface à partir de cleaned_df
    # win_probabilities = []
    # for index, row in merged_df.iterrows():
    #     player1 = row['Joueur']
    #     player2 = row['Adversaire']
    #     surface = cleaned_df['surface']  # Assurez-vous que 'surface' est bien une colonne dans cleaned_df
        
    #     # Calcul des probabilités de victoire avec la surface récupérée de cleaned_df
    #     win_prob_player1, win_prob_player2 = calculate_win_probability(player1, player2, surface, cleaned_df, stat)
        
    #     # Ajout des résultats à la liste des probabilités de victoire
    #     win_probabilities.append({
    #         'Joueur': player1,
    #         'Adversaire': player2,
    #         'Surface': surface,
    #         'Win Probability Joueur 1': win_prob_player1,
    #         'Win Probability Joueur 2': win_prob_player2
    #     })
    
    # # Ici, vous pouvez envoyer win_probabilities au front-end ou faire d'autres traitements selon vos besoins
    # print("Win Probabilities:")
    # print(win_probabilities)

if __name__ == "__main__":
    main()
