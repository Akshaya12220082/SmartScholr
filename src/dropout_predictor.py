# src/dropout_predictor.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_dropout_model(data_path="Data/dropout_risk.csv", save_path="Models/dropout_model.pkl"):
    df = pd.read_csv(data_path)
    
    X = df[['Attendance', 'GPA', 'Failures']]
    y = df['Dropout_Risk']   # Low, Medium, High

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    joblib.dump(model, save_path)
    print("✅ Dropout Model Saved!")

def predict_dropout(input_data, model_path="Models/dropout_model.pkl"):
    model = joblib.load(model_path)
    prediction = model.predict([input_data])
    return prediction[0]
