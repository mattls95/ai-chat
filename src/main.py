import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from model import init, generate_content, add_model_message

user_prompt = "Why is the sky blue?"
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

client = init()
response = generate_content(client, messages)

for candidate in response.candidates:
    add_model_message(messages, candidate.content)
    #print(candidate.content)

for message in messages:
    print(message)
