import pickle
import pandas as pd
from sentiment_analysis import analyze_sentiment
from feature_engineering import create_features

def prioritize_issues(model_path, new_complaints, kpi_data):
    """
    Predict severity for new complaints and prioritize them.
    """
    with open(model_path, 'rb') as f:
        clf = pickle.load(f)

    new_complaints = analyze_sentiment(new_complaints)
    X_new, _ = create_features(new_complaints, kpi_data)

    new_complaints['predicted_severity'] = pd.Series(clf.predict(X_new), index=new_complaints.index)

    return new_complaints.sort_values(by='predicted_severity', ascending=False)
#
