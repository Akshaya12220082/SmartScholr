# 🎓 SmartScholr – A Machine Learning–Powered Personalized Learning Assistant

> 🚀 A data-driven, intelligent learning platform that predicts student performance, delivers personalized micro-lessons, and tracks progress using ML, enriched with emotion-aware feedback, gamified milestones, and AI-enhanced support.

---

## 📘 Project Overview

**SmartScholr** is a smart EdTech capstone project focused on making learning deeply personalized and effective. It uses **Machine Learning** at its core to assess performance, generate improvement plans, and support students using **micro-learning**, **milestones**, and **emotion-aware feedback**.

Built as a modular, extensible system, SmartScholr includes both classic ML features and modern UI/UX improvements such as voice-based Q&A, pinned sticky notes, and AI-powered chat support.

---

## 🎯 Objectives

- Predict academic performance using ML models
- Detect students at risk of poor performance or dropout
- Deliver concept-wise **micro-study bubbles** (short 5-min lessons)
- Track student progress and **unlock milestone badges**
- Provide **emotion-aware feedback** using user interaction data
- Enable **voice-based Q&A** for accessibility
- Allow students to **pin notes/reminders/formulas** via sticky notes
- Deliver feedback using both ML insights and optional GenAI support

---

## 🧭 User Flow

1. **🔐 Login / Setup**
   - Enter basic details (name, grade/semester)

2. **📁 Upload Academic Data**
   - Upload marks, attendance, or manually enter key academic metrics

3. **🧪 Take Smart Assessment Test**
   - Auto-generated quiz by concept & difficulty
   - Auto-scoring + weak-topic detection

4. **📊 View ML-Powered Performance Dashboard**
   - See predicted scores, risk levels
   - Understand weak areas via SHAP explainability

5. **📘 Get Personalized Study Plan**
   - System recommends a **7-day study roadmap**
   - Each day has **micro-study bubbles** (5–7 minute lessons)

6. **💬 Ask AI Chatbot or Use Voice Q&A**
   - Ask doubts using text or **voice**
   - Get GenAI-based answers (optional OpenAI or local model)

7. **📌 Use Sticky Notes on Dashboard**
   - Students can pin reminders, formulas, or goals to the dashboard

8. **🏁 Unlock Milestones**
   - Earn badges for completing lessons/tests/plans
   - View **progress bars and performance trackers**

9. **😓 Emotion-Aware Feedback**
   - Detect signs of **confusion/frustration** based on interactions (e.g., repeated wrong attempts, time delays)
   - Recommend breaks or easier content

10. **📥 Export Report**
   - Weekly performance report (PDF or CSV)

---

## ✨ Key Features

### 🔹 Academic Performance Prediction *(ML Core)*
- Predicts student scores using XGBoost / Random Forest  
- Features: attendance, quiz scores, assignments

### 🔹 Dropout Risk Classification *(ML Core)*
- Classifies students as Low/Medium/High risk using Logistic Regression

### 🔹 Smart Assessment + Recovery Engine *(ML + Rule-Based)*
- Generates topic-wise quizzes
- Detects weak concepts
- Builds improvement plans

### 🔹 Micro-Study Bubbles *(UX + ML Integration)*
- Personalized 5-minute lessons based on weak concepts
- Delivered daily in the study plan

### 🔹 Study Plan Recommendation
- Auto-generates a 7-day plan with micro-tasks, resource links

### 🔹 SHAP Explainability
- ML dashboard shows why a prediction was made

### 🔹 Emotion-Aware Feedback *(UX + Optional Vision/NLP)*
- Detect confusion or frustration from:
  - Low accuracy in repeated attempts
  - Slow response time
- Triggers soft interventions (e.g., motivational pop-ups)

### 🔹 Milestone Trackers & Gamification
- Earn badges for:
  - Completing modules
  - Improving performance
- View progress timeline and unlock levels

### 🔹 Voice-Based Q&A 
- Ask academic questions using voice input
- Responds with audio/text answers using speech-to-text + OpenAI

### 🔹 Sticky Notes Dashboard
- Pin important formulas, reminders, motivational notes

### 🔹 AI Chatbot Assistant (GenAI)
- Ask academic questions in natural language
- Powered by GPT-3.5 or syllabus-trained LLMs
- Supports both MCQ generation and concept explanation

---

## ⚙️ Tech Stack

| Layer          | Tech Used                                                  |
|----------------|------------------------------------------------------------|
| UI/Frontend    | **Streamlit (Multi-page app)**                             |
| ML Models      | scikit-learn, XGBoost, SHAP, K-Means                       |
| NLP + Feedback | NLTK, spaCy, SHAP, LangChain (optional)                    |
| GenAI (Optional) | OpenAI API (GPT-3.5), Whisper for speech input            |
| Chatbot        | LangChain + syllabus-based Q&A system                      |
| Emotion Module | Time-delay + accuracy-based trigger (future: face capture) |
| Gamification   | Custom badge/level tracker in Streamlit                    |
| Backend        | Python, SQLite / Firebase                                  |
| Hosting        | Streamlit Cloud / Hugging Face Spaces                      |

---


