import requests
import pandas as pd
import sqlite3
from datetime import datetime

def fetch_and_save():
    url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/exports/json"
    try:
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        
        # --- Feature Engineering ---
        
        # 1. Extraction des coordonnées (souvent dans un dictionnaire 'coordonnees_geo')
        # L'API renvoie souvent un objet : {'lon': 2.34, 'lat': 48.85}
        df['lat'] = df['coordonnees_geo'].apply(lambda x: x['lat'] if isinstance(x, dict) else None)
        df['lon'] = df['coordonnees_geo'].apply(lambda x: x['lon'] if isinstance(x, dict) else None)
        
        # 2. Calcul du taux
        df['filling_rate'] = (df['numbikesavailable'] / df['capacity']).fillna(0)
        df['event_date'] = df['duedate']
        df['ingestion_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 3. Sélection des colonnes (Avec Lat/Lon cette fois)
        cols = [
            'stationcode', 
            'name', 
            'filling_rate', 
            'numbikesavailable', 
            'capacity',
            'lat',
            'lon',
            'event_date',      # <--- La vérité terrain (pour le Machine Learning)
            'ingestion_date'   # <--- L'audit technique (pour le Data Engineering)
        ]
        
        # On ne garde que les colonnes existantes (sécurité si l'API change légèrement)
        final_df = df[cols]
        
        # --- Stockage ---
        conn = sqlite3.connect("velib_data.db")
        final_df.to_sql("availabilities", conn, if_exists="append", index=False)
        conn.close()
        
        print(f"[{datetime.now()}] Ingestion réussie : {len(final_df)} stations avec GPS sauvegardées.")
        
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    fetch_and_save()