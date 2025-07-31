# src/quiz_engine.py
import pandas as pd
import random

def generate_quiz(num_questions=5):
    quiz_df = pd.read_csv("Data/quiz_bank.csv")
    return quiz_df.sample(n=num_questions).reset_index(drop=True)

def score_quiz(answers, correct_answers):
    score = sum([1 for a, b in zip(answers, correct_answers) if a == b])
    return score
