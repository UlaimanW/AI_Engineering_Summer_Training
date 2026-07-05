from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Give me 10 creative names for an AI app that helps computer science students learn AWS, Linux, and Python.",
    config=types.GenerateContentConfig(
        temperature=0.5
    )
    
)

print(response.text)