import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def list_available_gemini_models():
    print("Available Gemini models supporting generateContent:")
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(m.name)

if __name__ == "__main__":
    list_available_gemini_models()
