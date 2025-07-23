# app/mock_question_generator.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

# Load Gemini API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def generate_questions(resume_text):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        prompt = f"""
You are an AI interviewer. Read the resume below and generate 5 **mock interview questions**.
Return your response as a **JSON array**, like this:
["Question 1", "Question 2", ..., "Question 5"]

Resume:
\"\"\"
{resume_text}
\"\"\"
        """

        response = model.generate_content(prompt)
        raw = response.text.strip()

        print("\n📤 Gemini Raw Response:\n", raw)

        # Strip code block formatting if present
        if raw.startswith("```"):
            # Remove ```json or ``` and ending ```
            raw = raw.strip("`").split("json", 1)[-1].strip()
            raw = raw.strip("`").strip()

        # Now parse the cleaned JSON string
        questions = json.loads(raw)

        if isinstance(questions, list) and all(isinstance(q, str) for q in questions):
            return questions
        else:
            print("⚠️ Invalid format after parsing:", questions)
            return None

    except json.JSONDecodeError as json_err:
        print("❌ JSON parsing error:", json_err)
        return None
    except Exception as e:
        print("❌ Error in generate_questions:", e)
        return None
