# app/embedding_util.py

import os
from dotenv import load_dotenv
import google.generativeai as genai
import ast

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def get_embedding(text):
    try:
        # Use Gemini flash model
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        prompt = f"""
You are an AI assistant. Given the following resume text, generate a semantic vector embedding for it.
Return the result **only** as a list of floats like: [0.123, 0.456, ...] without any explanation or extra text.

Text:
\"\"\"{text}\"\"\"
        """

        # Generate response
        response = model.generate_content(prompt)
        cleaned = response.text.strip()

        print("\n🔍 Gemini Response:\n", cleaned)

        # Convert string to actual Python list
        embedding = ast.literal_eval(cleaned)

        if isinstance(embedding, list) and all(isinstance(x, (float, int)) for x in embedding):
            return embedding
        else:
            print("⚠️ Invalid format received:", cleaned)
            return None

    except Exception as e:
        print("❌ Error in get_embedding:", e)
        return None
