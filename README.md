# HydroGenesis: Smart Plant Watering System with Machine Learning

## 🌱 Project Overview
HydroGenesis is a smart plant watering system that predicts when to water a plant using sensor data and machine learning. The system uses an ESP32 microcontroller to collect data from soil moisture, temperature, humidity, and light sensors, which is then processed in the cloud to make watering decisions.

## 🚀 Features
- Collects real-time sensor data (moisture, temperature, humidity, light intensity).
- Uses a machine learning model to predict when watering is needed.
- Deploys the model on a cloud API for lightweight integration with ESP32.
- Blynk IoT integration for remote monitoring and control.

## 📁 Project Structure
```
HydroGenesis/
│── dataset/
│   ├── plant_watering_data.csv  # Generated dataset
│── models/
│   ├── trained_model.pkl        # Trained ML model
│── scripts/
│   ├── generate_dataset.py      # Script to create dataset
│   ├── train_model.py           # Train ML model and save it
│   ├── api_server.py            # FastAPI server to deploy the model
│── esp32_code/
│   ├── hydrogenesis.ino         # Arduino code for ESP32
│── README.md                    # Project documentation
```

## 📜 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/HydroGenesis.git
cd HydroGenesis
```

### 2️⃣ Generate Dataset
```bash
python scripts/generate_dataset.py
```

### 3️⃣ Train Machine Learning Model
```bash
python scripts/train_model.py
```

### 4️⃣ Deploy Cloud API
```bash
uvicorn scripts.api_server:app --host 0.0.0.0 --port 8000
```

### 5️⃣ Upload ESP32 Code
- Open `hydrogenesis.ino` in Arduino IDE
- Install required libraries (WiFi, Blynk, DHT, etc.)
- Upload to ESP32

## 🆓 Free Cloud Platforms
- **Google Colab** (for training ML models)
- **Deta Space** or **Render** (for hosting API)
- **Blynk Free Plan** (for IoT monitoring)

## 👨‍💻 Contributions
Contributions are welcome! Feel free to submit issues and pull requests.

## 📜 License
This project is open-source under the MIT License.

🚀 Happy Coding!

