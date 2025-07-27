import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def init():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    return client

def add_model_message(messages, content ):
    messages.append(content)

def generate_content(client, messages):
    response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=messages
    )   
    return response