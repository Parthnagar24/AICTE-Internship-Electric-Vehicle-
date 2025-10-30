
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

# Paths
BASE = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE, "data", "ev_dataset.csv")
MODEL_PATH = os.path.join(BASE, "model", "ev_range_model.pkl")

def load_data():
    df = pd.read_csv(DATA_PATH)
    return df

def train_and_save():
    df = load_data()
    X = df[["battery_percent", "speed_kmh", "temperature_c"]]
    y = df["actual_range_km"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("MSE:", mean_squared_error(y_test, preds))
    print("R2 :", r2_score(y_test, preds))
    joblib.dump(model, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save()
