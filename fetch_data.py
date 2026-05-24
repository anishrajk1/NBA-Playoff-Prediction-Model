from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import time
import os

os.makedirs("data", exist_ok=True)

seasons = [
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24"
]

all_games = []

for season in seasons:
    print("Downloading:", season)

    gf = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        season_type_nullable="Playoffs"
    )

    df = gf.get_data_frames()[0]
    all_games.append(df)

    time.sleep(1)

final_df = pd.concat(all_games)

final_df.to_csv("data/playoff_games_raw.csv", index=False)

print("Done. Data saved in data/playoff_games_raw.csv")