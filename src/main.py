import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#user_prompt = input("Enter prompt: ")
user_prompt = "Why is the sky blue?"

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
)

for candidate in response.candidates:
    print(candidate.content)

#print(response.text)