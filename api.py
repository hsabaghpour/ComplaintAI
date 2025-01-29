from fastapi import FastAPI
import pandas as pd
from prioritization import prioritize_issues

app = FastAPI()

@app.post("/predict/")
async def predict_complaint(data: dict):
    """
    API endpoint to predict complaint severity.
    """
    new_complaints = pd.DataFrame([data])
    kpi_data = pd.read_csv('data/kpi_data.csv')

    prioritized_complaints = prioritize_issues("models/classifier.pkl", new_complaints, kpi_data)

    return prioritized_complaints.to_dict(orient="records")
#
