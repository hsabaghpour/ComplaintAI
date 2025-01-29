
import pandas as pd
from data_loader import load_data
from sentiment_analysis import analyze_sentiment
from feature_engineering import create_features
from classifier import classify_complaints
from prioritization import prioritize_issues

if __name__ == "__main__":
    complaints, kpi_data = load_data('data/customer_complaints.csv', 'data/kpi_data.csv')
    complaints = analyze_sentiment(complaints)
    X, y = create_features(complaints, kpi_data)
    clf = classify_complaints(X, y, model_path="models/classifier.pkl")
    new_complaints = pd.read_csv('data/new_complaints.csv')
    prioritized_complaints = prioritize_issues("models/classifier.pkl", new_complaints, kpi_data)
    prioritized_complaints.to_csv('data/prioritized_complaints.csv', index=False)
    #main
