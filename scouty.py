import soccerdata as sd
import pandas as pd

LIGAS = [
    'ENG-Premier League',
    'ESP-La Liga',
    'FRA-Ligue 1',
    'GER-Bundesliga',
    'ITA-Serie A'
]

print("Bajando datos FBref 2026/27...")
fbref = sd.FBref(leagues=LIGAS, seasons="2026-2027")

df = fbref.read_player_season_stats(stat_type="standard")
print(f"Encontrados {len(df)} jugadores")

df.to_json("datos_26-27.json", orient="records", indent=2, force_ascii=False)
print("¡Hecho! Archivo datos_26-27.json creado")
