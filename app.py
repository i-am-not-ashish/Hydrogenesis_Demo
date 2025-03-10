from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Plant Watering Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # Extract features from request
    features = np.array([[data["moisture"], data["temperature"], data["humidity"], data["light_intensity"]]])

    # Make prediction
    prediction = model.predict(features)[0]

    return jsonify({"water_needed": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
