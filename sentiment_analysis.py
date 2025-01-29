from transformers import pipeline
import pandas as pd

# Load sentiment analysis model
sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

def analyze_sentiment(complaints):
    """
    Perform batch sentiment analysis on customer complaints.
    """
    complaints['complaint_text'] = complaints['complaint_text'].fillna('')

    # Batch processing for speed optimization
    texts = complaints['complaint_text'].tolist()
    sentiment_results = sentiment_analyzer(texts, batch_size=16)

    # Extract labels & scores
    complaints['sentiment'] = [res['label'] for res in sentiment_results]
    complaints['sentiment_score'] = [res['score'] for res in sentiment_results]

    # Map sentiment labels to numerical values
    sentiment_map = {'POSITIVE': 1, 'NEGATIVE': -1}
    complaints['sentiment_numeric'] = complaints['sentiment'].map(sentiment_map).fillna(0)

    return complaints
#
