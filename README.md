# 🤖 AI Resume Matcher for ATS

An intelligent Streamlit-based tool that compares your resume against a job description and provides:
- ✅ Match Score
- 🔍 Matched vs Missing Keywords
- 💡 AI-powered Resume Optimization Tips

Built using Python, NLP, and OpenAI GPT — perfect for job seekers and resume reviewers.

---

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🧠 Features

- 📄 **Resume Parsing (PDF)** using PyMuPDF
- 📋 **Job Description Analysis** (TXT)
- 📊 **TF-IDF Matching** for score calculation
- 🧩 **Keyword Comparison**: highlights matched & missing terms
- 🤖 **OpenAI GPT Feedback**: personalized resume improvement suggestions

---

## 🖥️ Live Demo

> You can run this locally with just one command (see below). Deployment to Streamlit Cloud or Render coming soon.

---

## 🚀 How to Run

### 1. Clone the repo
git clone https://github.com/your-username/resume-matcher-ai.git
cd resume-matcher-ai

### 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux


### 3. Install dependencies
pip install -r requirements.txt

### 4. Download spaCy model
python -m spacy download en_core_web_sm

### 5. Run the Streamlit app
streamlit run main.py


### Built With :

Streamlit

Python

spaCy

scikit-learn

OpenAI GPT

sentence-transformers
