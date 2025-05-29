import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_match_score(resume_text, jd_text):
    documents = [resume_text, jd_text]
    tfidf = TfidfVectorizer(stop_words="english").fit_transform(documents)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return round(score[0][0] * 100, 2)

def extract_keywords(text):
    words = re.findall(r'\b\w{4,}\b', text.lower())
    return set(words)

def get_keyword_diff(resume_text, jd_text):
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)
    matched = resume_keywords & jd_keywords
    missing = jd_keywords - resume_keywords
    return list(matched), list(missing)