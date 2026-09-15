import soccerdata as sd
import pandas as pd

LIGAS = ["ENG-Premier League", "ESP-La Liga", "ITA-Serie A", "GER-Bundesliga", "FRA-Ligue 1", "INT-Champions League"]
fbref = sd.FBref(leagues=LIGAS, seasons="26-27")

standard = fbref.read_player_season_stats(stat_type="standard")
shooting = fbref.read_player_season_stats(stat_type="shooting")
passing = fbref.read_player_season_stats(stat_type="passing")
defense = fbref.read_player_season_stats(stat_type="defense")
jugadores = pd.concat([standard, shooting, passing, defense], axis=1)
jugadores = jugadores.loc[:,~jugadores.columns.duplicated()]
jugadores.to_json("jugadores_campo_26_27.json", orient="records")
jugadores.to_csv("jugadores_campo_26_27.csv")

keepers = fbref.read_player_season_stats(stat_type="keeper")
keepers.to_json("porteros_26_27.json", orient="records")

equipos = fbref.read_team_season_stats(stat_type="standard")
equipos.to_json("equipos_26_27.json", orient="records")
