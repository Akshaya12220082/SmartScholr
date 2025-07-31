# src/score_predictor.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_score_model(data_path="Data/academic_data.csv", save_path="Models/academic_score_model.pkl"):
    df = pd.read_csv(data_path)
    
    X = df[['Attendance', 'Assignment_Score', 'Quiz_Score']]
    y = df['Final_Score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, save_path)
    print("✅ Academic Score Model Saved!")

def predict_score(input_data, model_path="Models/academic_score_model.pkl"):
    model = joblib.load(model_path)
    prediction = model.predict([input_data])
    return prediction[0]
