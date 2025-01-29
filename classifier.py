import pickle
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def classify_complaints(X, y, model_path="models/classifier.pkl"):
    """
    Train an XGBoost classifier to categorize complaints.
    """
    if y is None:
        raise ValueError("Target variable 'severity' is missing")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save the trained model
    with open(model_path, 'wb') as f:
        pickle.dump(clf, f)

    return clf
#
