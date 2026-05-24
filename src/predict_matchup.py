import joblib
import numpy as np

model = joblib.load("models/real_nba_model.pkl")

print("NBA MATCHUP PREDICTOR")
print("----------------------")

print("\nEnter Team A stats:")
a_w_pct = float(input("W_PCT: "))
a_pts = float(input("PTS: "))
a_fg = float(input("FG_PCT: "))
a_fg3 = float(input("FG3_PCT: "))
a_reb = float(input("REB: "))
a_ast = float(input("AST: "))
a_tov = float(input("TOV: "))
a_pm = float(input("PLUS_MINUS: "))

print("\nEnter Team B stats:")
b_w_pct = float(input("W_PCT: "))
b_pts = float(input("PTS: "))
b_fg = float(input("FG_PCT: "))
b_fg3 = float(input("FG3_PCT: "))
b_reb = float(input("REB: "))
b_ast = float(input("AST: "))
b_tov = float(input("TOV: "))
b_pm = float(input("PLUS_MINUS: "))

#build diff features (A - B)
X = np.array([[
    a_w_pct - b_w_pct,
    a_pts - b_pts,
    a_fg - b_fg,
    a_fg3 - b_fg3,
    a_reb - b_reb,
    a_ast - b_ast,
    a_tov - b_tov,
    a_pm - b_pm
]])

pred = model.predict(X)[0]
prob = model.predict_proba(X)[0][1]

print("\n----------------------")

if pred == 1:
    print("Prediction: Team A Wins")
else:
    print("Prediction: Team B Wins")

print(f"Win Probability (Team A): {prob * 100:.2f}%")
