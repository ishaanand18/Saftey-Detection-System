# 🛡️ Safety Detection & Risk Prediction System

An end-to-end Machine Learning web application that predicts the safety level of Indian locations based on user inputs such as city, time, age, and gender.

The system uses a Random Forest Classifier to estimate safety risk and displays results using confidence scores and Safe/Unsafe probability percentages.  

Additionally, it integrates an Ollama-based AI Safety Chatbot to provide contextual safety guidance and interaction.

---

## 🚀 Features

- 📍 Location-based safety prediction
- 🕒 Time-aware risk estimation
- 👤 Age & Gender contextual analysis
- 🌲 Random Forest classification model
- 📊 Confidence score display
- 📈 Safe vs Unsafe probability percentages
- 🤖 Ollama-powered Safety Chatbot
- 📝 Prediction logging to CSV
- 🌐 Flask-based web interface

---

## 🧠 Machine Learning Model

- Model Used: Random Forest Classifier
- Problem Type: Binary Classification

### Input Features:
- City
- Time
- Age
- Gender

### Output:
- Safe (0)
- Unsafe (1)
- Confidence Score
- Safe Probability (%)
- Unsafe Probability (%)

The model was trained on structured safety-related data and optimized for improved reliability and reduced overfitting using ensemble learning.

---

## 🤖 AI Safety Chatbot

The system includes a locally powered chatbot built using Ollama.

### Chatbot Capabilities:
- Provides safety-related suggestions
- Offers precautionary guidance based on user queries
- Enhances user engagement
- Demonstrates integration of Generative AI into a traditional ML pipeline

---

## 🏗️ Tech Stack

### 🔹 Backend
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

### 🔹 Machine Learning
- Random Forest (Ensemble Learning)

### 🔹 Generative AI
- Ollama (Local LLM Integration)

### 🔹 Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

Safety-Detection-System/
│
├── app.py
├── model.pkl
├── chatbot.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   ├── js/
│
├── dataset/
├── logs/
│   └── predictions.csv
└── README.md

---

## ⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/yourusername/Safety-Detection-System.git

2. Navigate into the directory

cd Safety-Detection-System

3. Install dependencies

pip install -r requirements.txt

4. Ensure Ollama is installed and running locally

5. Run the Flask application

python app.py

6. Open in browser

http://127.0.0.1:5000/

---

## 📊 How It Works

1. User enters:
   - City
   - Time
   - Age
   - Gender

2. Input data is preprocessed and encoded.
3. Random Forest model predicts:
   - Safety classification
   - Probability scores
4. System displays:
   - Safe/Unsafe label
   - Confidence score
   - Probability percentages
5. Users can interact with the AI Safety Chatbot for guidance.

---

## 🎯 What This Project Demonstrates

- End-to-end ML deployment
- Ensemble learning implementation
- Model probability interpretation
- Flask-based backend development
- Integration of Generative AI (Ollama)
- Structured logging & data tracking

---

## 📈 Future Improvements

- Hyperparameter tuning
- Real-time crime dataset integration
- Deployment on cloud platform
- User authentication system
- Feedback-based model retraining
