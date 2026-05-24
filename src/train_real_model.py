import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

#load dataset
df = pd.read_csv("data/real_matchup_dataset.csv")

features = [
    "W_PCT_DIFF",
    "PTS_DIFF",
    "FG_PCT_DIFF",
    "FG3_PCT_DIFF",
    "REB_DIFF",
    "AST_DIFF",
    "TOV_DIFF",
    "PLUS_MINUS_DIFF"
]

X = df[features]
y = df["A_WIN"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

#train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

#eval
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print("Real Model Accuracy:", round(acc * 100, 2), "%")

#save
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/real_nba_model.pkl")

print("Saved: models/real_nba_model.pkl")
