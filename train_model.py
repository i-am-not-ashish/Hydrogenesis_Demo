import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("plant_watering_data.csv")  # Make sure this dataset is in the same folder

# Features & Target
X = df[['Moisture', 'Temperature', 'Humidity', 'Light_Intensity']]
y = df['Water_Needed']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=10, max_depth=3)
model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved successfully!")
