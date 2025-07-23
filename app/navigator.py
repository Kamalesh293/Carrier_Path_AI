from resume_parser import extract_text
from embedding_util import get_embedding
from compare import cosine_similarity
from skill_matcher import match_skills
from skill_resources import get_learning_resources
from mock_question_generator import generate_questions

import json
import os

# 📂 File paths
resume_path = "resumes/kamalesh_resume.txt"  # ✅ Your saved resume
job_role_template_path = "roles/data_analyst_template.json"

# 📥 Step 1: Extract resume text
resume_text = extract_text(resume_path)

# 📥 Step 2: Load job role template
with open(job_role_template_path, "r", encoding="utf-8") as f:
    job_data = json.load(f)
job_description = job_data["description"]
required_skills = job_data["skills"]

# 🔢 Step 3: Convert to embeddings
resume_embed = get_embedding(resume_text)
role_embed = get_embedding(job_description)

# 📐 Step 4: Compare embeddings
similarity = cosine_similarity(resume_embed, role_embed)
match_score = round(similarity * 100, 2)

# ✅ Step 5: Skill matching
matched, missing = match_skills(resume_text, required_skills)

# 📚 Step 6: Learning resource suggestions
resources = get_learning_resources(missing)

# 🎤 Step 7: Generate mock interview questions
questions = generate_questions(missing)

# 📄 Step 8: Save output
os.makedirs("outputs", exist_ok=True)

with open("outputs/gap_analysis.txt", "w", encoding="utf-8") as f:
    f.write(f"🎯 Target Role: {job_data['role']}\n")
    f.write(f"📊 Resume Match Score: {match_score}%\n")
    f.write(f"\n✅ Matched Skills:\n{', '.join(matched)}\n")
    f.write(f"\n❌ Missing Skills:\n{', '.join(missing)}\n")
    f.write("\n📚 Suggested Learning Resources:\n")
    for skill, link in resources.items():
        f.write(f"- {skill}: {link}\n")

with open("outputs/interview_questions.txt", "w", encoding="utf-8") as f:
    f.write("🎤 Mock Interview Questions:\n\n")
    for q in questions:
        f.write(f"- {q}\n")

print("✅ Analysis complete! Check the 'outputs/' folder for results.")
