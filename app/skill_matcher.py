from difflib import get_close_matches

# Predefined job description skills for Data Scientist
job_skills = [
    "Python", "SQL", "Machine Learning", "Data Analysis", "NLP",
    "Pandas", "NumPy", "Scikit-learn", "Matplotlib",
    "Streamlit", "OpenAI API", "Gemini API", "Resume Parsing",
    "Vector Embeddings", "Cosine Similarity", "FastAPI", "Docker"
]

def extract_skills_from_resume(resume_text):
    resume_text_lower = resume_text.lower()
    matched = []
    for skill in job_skills:
        if skill.lower() in resume_text_lower:
            matched.append(skill)
    return matched

def analyze_skills(resume_text, job_desc):
    matched_skills = extract_skills_from_resume(resume_text)
    missing_skills = [skill for skill in job_skills if skill not in matched_skills]

    # Basic Resume Score
    resume_score = round((len(matched_skills) / len(job_skills)) * 100)

    # Generate Learning Advice
    if missing_skills:
        learning_advice = f"To improve your resume, consider learning: {', '.join(missing_skills)}. You can explore them using online platforms like Coursera, Udemy, or YouTube."
    else:
        learning_advice = "Excellent! Your resume covers most key skills for this role."

    return matched_skills, missing_skills, learning_advice, resume_score
