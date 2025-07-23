import streamlit as st
import os
from dotenv import load_dotenv
from app.embedding_util import get_embedding
from app.mock_question_generator import generate_questions
from app.skill_matcher import analyze_skills

load_dotenv()

st.set_page_config(page_title="CareerPathAI - Resume Analyzer", layout="centered")

st.title("🎯 CareerPathAI")
st.subheader("Get Personalized Career Guidance Based on Your Resume")

# Predefined Job Description (used internally)
default_job_description = """
We are looking for a Data Scientist with experience in Python, Machine Learning, Data Analysis, 
Natural Language Processing (NLP), and working with APIs like OpenAI or Gemini. 
Familiarity with Streamlit, Scikit-learn, Pandas, and SQL is a plus.
"""

# Resume Upload
uploaded_file = st.file_uploader("📄 Upload your Resume (Text or PDF)", type=["txt", "pdf"])

if uploaded_file is not None:
    try:
        resume_text = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error("❌ Error reading file.")
        st.code(str(e))
    else:
        st.markdown("#### 📝 Resume Preview")
        st.text_area("Your Resume Content", value=resume_text, height=300)

        if st.button("🔍 Analyze My Resume"):
            with st.spinner("Analyzing your resume..."):
                resume_embedding = get_embedding(resume_text)

                if resume_embedding:
                    st.success("✅ Embedding Generated Successfully")

                    try:
                        # Analyze skills
                        matched_skills, missing_skills, learning_advice, resume_score = analyze_skills(
                            resume_text, default_job_description
                        )

                        # 📈 Resume Score
                        st.markdown(f"### 📈 Resume Score: **{resume_score}%**")

                        # ✅ Matched Skills
                        st.markdown("#### ✅ Matched Skills")
                        if matched_skills:
                            for skill in matched_skills:
                                st.success(f"• {skill}")
                        else:
                            st.info("No strong matches found.")

                        # ❌ Missing Skills
                        st.markdown("#### ❌ Missing Skills")
                        if missing_skills:
                            for skill in missing_skills:
                                st.error(f"• {skill}")
                        else:
                            st.success("No major missing skills. Great job!")

                        # 📚 Learning Advice
                        st.markdown("#### 📚 Learning Advice")
                        st.info(learning_advice if learning_advice else "No suggestions provided.")

                    except Exception as e:
                        st.error("❌ Failed to analyze skills.")
                        st.code(str(e), language="python")

                    # 🎤 Mock Interview Questions
                    questions = generate_questions(resume_text)
                    if questions:
                        st.markdown("#### 🎤 Mock Interview Questions")
                        for q in questions:
                            st.write(f"• {q}")
                    else:
                        st.warning("⚠️ No questions generated. Check LLM API logic.")
                else:
                    st.error("❌ Failed to generate embedding. Check your API or model.")
