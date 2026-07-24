import joblib

# Load trained model and vectorizer
model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

print("=" * 50)
print("      ROOT CAUSE PREDICTION SYSTEM")
print("=" * 50)

while True:

    message = input("\nEnter Log Message (or type 'exit'): ")

    if message.lower() == "exit":
        print("\nExiting...")
        break

    # Convert message into vector
    message_vector = vectorizer.transform([message])

    # Predict root cause
    prediction = model.predict(message_vector)

    # Prediction probability
    probability = model.predict_proba(message_vector)

    confidence = max(probability[0]) * 100

    print("\nPredicted Root Cause :", prediction[0])
    print(f"Confidence           : {confidence:.2f}%")