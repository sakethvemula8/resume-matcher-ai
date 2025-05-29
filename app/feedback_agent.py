import openai

def generate_feedback(resume_text, jd_text):
    prompt = f"""
You are a resume optimization expert.
Given this resume: {resume_text[:1500]}
And this job description: {jd_text[:1500]}
Give 3 bullet-point suggestions to improve the resume to match the job description better.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You're a helpful and concise resume coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
