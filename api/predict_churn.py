from http.server import BaseHTTPRequestHandler
import json
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Global model instance cached across invocations
MODEL = None

def _paths():
    base_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(base_dir, ".."))
    data_path = os.path.join(root_dir, "app", "churn_data.csv")
    model_path = os.path.join(root_dir, "app", "churn_model.pkl")
    return data_path, model_path

def _load_or_train():
    global MODEL
    data_path, model_path = _paths()

    try:
        MODEL = joblib.load(model_path)
        return
    except Exception:
        pass

    df = pd.read_csv(data_path)
    X = df[["age", "subscription_months", "login_freq"]]
    y = df["churned"]

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    MODEL = model
    try:
        joblib.dump(model, model_path)
    except Exception:
        # Ignore persistence errors in serverless environment
        pass

# Warm model at import time (reduces cold-start latency on first request)
_load_or_train()

def _predict_probability(age: int, subscription_months: int, login_freq: int) -> float:
    features = np.array([[age, subscription_months, login_freq]])
    return float(MODEL.predict_proba(features)[0][1])

class handler(BaseHTTPRequestHandler):
    def _set_headers(self, status: int = 200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length) if content_length > 0 else b"{}"
            body = json.loads(raw_body.decode("utf-8") or "{}")

            age = int(body.get("age"))
            subscription_months = int(body.get("subscription_months"))
            login_freq = int(body.get("login_freq"))

            probability = round(_predict_probability(age, subscription_months, login_freq), 3)
            self._set_headers(200)
            self.wfile.write(json.dumps({"churn_probability": probability}).encode("utf-8"))
        except Exception as exc:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": str(exc)}).encode("utf-8"))
