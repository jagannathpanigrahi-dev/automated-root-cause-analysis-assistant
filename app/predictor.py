import joblib

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


def predict_root_cause(message: str):

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)[0]

    confidence = max(model.predict_proba(message_vector)[0]) * 100

    return {
        "root_cause": prediction,
        "confidence": round(confidence, 2)
    }