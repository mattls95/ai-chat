from google import genai
from google.genai import types

def add_user_message(messages, content):
    messages.append(types.Content(role="user", parts=[types.Part(text=content)]))

def generate_input():
    content = input("> ")
    return content