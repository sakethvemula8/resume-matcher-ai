import streamlit as st
from app.resume_parser import extract_resume_text
from app.jd_parser import extract_jd_text
from app.matcher import compute_match_score, get_keyword_diff
from app.feedback_agent import generate_feedback

st.title("AI Resume Matcher for ATS")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_file = st.file_uploader("Upload Job Description (TXT)", type=["txt"])

if resume_file and jd_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(resume_file.read())
    with open("temp_jd.txt", "wb") as f:
        f.write(jd_file.read())

    resume_text = extract_resume_text("temp_resume.pdf")
    jd_text = extract_jd_text("temp_jd.txt")

    score = compute_match_score(resume_text, jd_text)
    st.metric(label="Match Score", value=f"{score}%")

    matched, missing = get_keyword_diff(resume_text, jd_text)
    st.subheader("Matched Keywords")
    st.write(matched[:20])

    st.subheader("Missing Keywords")
    st.write(missing[:20])

    if st.button("Generate AI Resume Feedback"):
        with st.spinner("Analyzing with GPT..."):
            feedback = generate_feedback(resume_text, jd_text)
            st.subheader("AI Feedback")
            st.markdown(feedback)