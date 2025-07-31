# src/data_utils.py
import pandas as pd

def load_academic_data():
    return pd.read_csv("Data/academic_data.csv")

def load_dropout_data():
    return pd.read_csv("Data/dropout_risk.csv")

def load_quiz_bank():
    return pd.read_csv("Data/quiz_bank.csv")

def load_quiz_results():
    return pd.read_csv("Data/quiz_results.csv")

def preprocess_academic(df):
    # Example preprocessing
    df = df.dropna()
    df['Attendance'] = df['Attendance'].clip(0, 100)  # limit to 0–100
    return df
