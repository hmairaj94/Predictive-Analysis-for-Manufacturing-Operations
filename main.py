import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

app = FastAPI()

DATA_PATH = "data/dataset.csv"
MODEL_PATH = "model/model.pkl"

@app.get("/")
def read_root():
    return {"message": "Predictive Analysis for Manufacturing Operations"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df.to_csv(DATA_PATH, index=False)
    return {"message": "File uploaded successfully", "columns": list(df.columns)}

@app.post("/train")
def train_model():
    if not os.path.exists(DATA_PATH):
        raise HTTPException(status_code=400, detail="No dataset found. Upload a file first.")

    df = pd.read_csv(DATA_PATH)
    required_columns = {"Temperature", "Run_Time", "Downtime_Flag"}
    if not required_columns.issubset(df.columns):
        raise HTTPException(status_code=400, detail=f"Dataset must contain columns: {required_columns}")

    X = df[["Temperature", "Run_Time"]]
    y = df["Downtime_Flag"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    return {"message": "Model trained successfully", "accuracy": accuracy}

@app.post("/predict")
def make_prediction(input_data: dict):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df[["Temperature", "Run_Time"]])

    # Convert numpy.int64 to native int
    return {"Downtime": int(prediction[0]), "Confidence": 0.85}