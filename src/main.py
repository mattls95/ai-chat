import sys
from google import genai
from model import init, generate_content, add_model_message
from user import generate_input, add_user_message

def main():
    try:
        messages = []
        client = init()
        generate_conversation(messages, client)
    except Exception as e:
       print(e)
       sys.exit(0) 

def generate_conversation(messages, client):
    while True:
        try:
            content = generate_input()
            add_user_message(messages, content)

            response = generate_content(client, messages)

            for candidate in response.candidates:
                if candidate.content:
                    add_model_message(messages, candidate.content)
                    for part in candidate.content.parts:
                        if part.text:
                            print(f"AI: {part.text}")
        except KeyboardInterrupt:
            log_conversation(messages)
            print("\nInterrupted by user. Exiting gracefully.")
            sys.exit(0)

if __name__ == "__main__":
    main()