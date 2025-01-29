import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer

def create_features(complaints, kpi_data):
    """
    Combine sentiment scores with KPI data and add NLP features.
    """
    if 'area_id' not in complaints.columns or 'area_id' not in kpi_data.columns:
        raise KeyError("Missing 'area_id' column in one of the datasets")

    merged_data = pd.merge(complaints, kpi_data, on='area_id', how='inner')

    # TF-IDF Feature Extraction
    vectorizer = TfidfVectorizer(max_features=100)
    tfidf_matrix = vectorizer.fit_transform(merged_data['complaint_text']).toarray()

    # New Features
    merged_data['complaint_length'] = merged_data['complaint_text'].apply(lambda x: len(str(x)))
    
    # Required Features
    kpi_features = ['access_issue', 'drop_call_rate', 'voice_quality_score', 'data_throughput']
    all_features = ['sentiment_numeric', 'complaint_length'] + kpi_features

    # Combine TF-IDF with structured data
    X_structured = merged_data[all_features].values
    X = np.hstack((X_structured, tfidf_matrix))

    y = merged_data['severity'] if 'severity' in merged_data.columns else None

    # Standardize numerical features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y
#
#