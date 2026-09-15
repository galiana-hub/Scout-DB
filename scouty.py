import soccerdata as sd

LIGAS = [
    'ENG-Premier League',
    'ESP-La Liga',
    'FRA-Ligue 1',
    'GER-Bundesliga',
    'ITA-Serie A'
]

# 2026/27 -> FBref lo quiere así: 2026-2027
fbref = sd.FBref(leagues=LIGAS, seasons="2026-2027")

df = fbref.read_player_season_stats(stat_type="standard")
print(f"Jugadores encontrados: {len(df)}")

df.to_json("datos_26-27.json", orient="records", indent=2)
print("JSON guardado!")
