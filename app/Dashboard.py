# app/Dashboard.py
import streamlit as st
from src.score_predictor import predict_score
from src.dropout_predictor import predict_dropout

st.title("📊 SmartScholr Dashboard")

attendance = st.slider("Attendance %", 0, 100, 75)
assignment = st.number_input("Assignment Score", 0, 100, 60)
quiz = st.number_input("Quiz Score", 0, 100, 50)
gpa = st.number_input("GPA", 0.0, 10.0, 7.0)
failures = st.number_input("No. of Failures", 0, 5, 0)

if st.button("Predict Performance"):
    score = predict_score([attendance, assignment, quiz])
    dropout = predict_dropout([attendance, gpa, failures])
    
    st.success(f"Predicted Final Score: {score:.2f}")
    st.warning(f"Dropout Risk: {dropout}")
