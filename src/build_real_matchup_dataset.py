import pandas as pd

games = pd.read_csv("data/playoff_games_raw.csv")
teams = pd.read_csv("data/team_strength.csv")

#only stable season level stats
team_cols = [
    "TEAM_ID",
    "TEAM_NAME",
    "W_PCT",
    "PTS",
    "FG_PCT",
    "FG3_PCT",
    "REB",
    "AST",
    "TOV",
    "PLUS_MINUS"
]

teams = teams[team_cols].drop_duplicates()

matchups = []

for game_id, group in games.groupby("GAME_ID"):
    if len(group) != 2:
        continue

    a = group.iloc[0]
    b = group.iloc[1]

    a_stats = teams[teams["TEAM_ID"] == a["TEAM_ID"]]
    b_stats = teams[teams["TEAM_ID"] == b["TEAM_ID"]]

    if a_stats.empty or b_stats.empty:
        continue

    a_stats = a_stats.iloc[0]
    b_stats = b_stats.iloc[0]

    matchups.append({
        "W_PCT_DIFF": a_stats["W_PCT"] - b_stats["W_PCT"],
        "PTS_DIFF": a_stats["PTS"] - b_stats["PTS"],
        "FG_PCT_DIFF": a_stats["FG_PCT"] - b_stats["FG_PCT"],
        "FG3_PCT_DIFF": a_stats["FG3_PCT"] - b_stats["FG3_PCT"],
        "REB_DIFF": a_stats["REB"] - b_stats["REB"],
        "AST_DIFF": a_stats["AST"] - b_stats["AST"],
        "TOV_DIFF": a_stats["TOV"] - b_stats["TOV"],
        "PLUS_MINUS_DIFF": a_stats["PLUS_MINUS"] - b_stats["PLUS_MINUS"],
        "A_WIN": 1 if a["WL"] == "W" else 0
    })

df = pd.DataFrame(matchups)
df.to_csv("data/real_matchup_dataset.csv", index=False)

print("Saved dataset:", df.shape)
