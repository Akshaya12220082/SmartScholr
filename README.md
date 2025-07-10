# SmartScholr

# 🎓 SmartScholr – A Machine Learning–Powered Personalized Learning Assistant

> 🚀 A capstone project blending Machine Learning with optional Generative AI to create a smart education assistant that predicts performance, detects weaknesses, and builds personalized study plans for students.

---

## 📘 Project Overview

**SmartScholr** is an intelligent educational platform designed to support students in their academic journey. At its core, the system uses **machine learning** to:

- Predict student performance
- Identify students at risk of failure or dropout
- Deliver concept-wise assessments
- Recommend tailored study plans
- Track progress over time

To make learning more interactive and personalized, the system optionally includes a **GenAI chatbot** trained on academic content to answer student queries and explain difficult concepts.

---

## 🎯 Objectives

- 📈 Predict student performance using academic history
- ⚠️ Identify at-risk learners using classification models
- 🧪 Auto-generate and score quizzes
- 📉 Detect weak topics based on assessment results
- 🗓️ Recommend personalized study plans
- 💬 Provide AI-powered concept explanations 
- 📊 Track learning progress and show improvements

---

## 🧭 User Flow

1. **Login / Student Details**  
   - Enter name, grade, or semester details

2. **Upload Academic History / Fill Form**  
   - Provide marks, attendance, or previous semester scores  
   - ML predicts performance & flags dropout risk

3. **Take AI-Generated Assessment**  
   - System creates a short topic-wise quiz  
   - Student answers questions in-app

4. **View ML-Powered Dashboard**  
   - Predicted scores, risk level  
   - Weak topics and SHAP explainability graphs

5. **Receive Personalized Study Plan**  
   - A 7-day schedule based on weak concepts  
   - Day-wise topics, durations, resource links

6. **Ask the AI Chatbot**  
   - Query about any concept or topic  
   - *"Explain derivatives with a real-life example"*  
   - *"Give me 3 MCQs on heat transfer"*

7. **Progress Tracking & Report Generation**  
   - Retake quizzes after a week  
   - View improvement over time  
   - Download a performance report (PDF/CSV)

---

## ✨ Key Features

### 🔹 1. Academic Performance Predictor *(ML Core)*
Uses regression models (Linear Regression, Random Forest, or XGBoost) to predict future academic scores based on attendance, previous marks, and activity data.

### 🔹 2. Dropout Risk Classifier *(ML Core)*
Classifies students into Low / Medium / High dropout risk categories using Logistic Regression or Decision Tree.

### 🔹 3. Learning Style Clustering *(ML Core)*
Clusters students based on behavioral data (e.g., time spent per subject, test score trends) using K-Means to personalize study materials.

### 🔹 4. Smart Assessment + Recovery Engine *(ML Core + Rule-Based)*
- Auto-generates quizzes based on selected topics  
- Scores answers automatically  
- Detects weak concepts  
- Generates a personalized 7-day recovery plan  
- Suggests relevant resources (YouTube links, PDFs)

### 🔹 5. Explainable ML Dashboard *(XAI)*
- SHAP or LIME visualizations to show why a student was predicted to be at risk  
- Builds trust in model predictions

### 🔹 6. AI Chatbot Tutor *(GenAI)*
- Powered by LangChain + OpenAI GPT  
- Students can ask doubts and get explanations  
- Optionally trained on syllabus PDFs for domain-specific answers

---

## ⚙️ Tech Stack

| Layer         | Tools/Libraries                                 |
|---------------|--------------------------------------------------|
| 👨‍💻 UI / App | **Streamlit** (multi-page app)                  |
| 🧠 ML Models  | scikit-learn, XGBoost, LightGBM, SHAP            |
| 🧪 NLP        | spaCy, NLTK                                      |
| 💬 GenAI (Optional) | OpenAI GPT-3.5/4, LangChain, T5/BART         |
| 🧾 Database   | SQLite (or Firebase for future scalability)       |
| 📊 Visualization | Matplotlib, Seaborn, Plotly                    |
| 🧰 Deployment | Streamlit Cloud / Hugging Face Spaces (optional) |

---


