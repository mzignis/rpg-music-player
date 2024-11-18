import json
import os
from pathlib import Path

import openai
import requests
from dotenv import load_dotenv
from tools.errors import ERRORS


# -------- load dot-env --------
load_dotenv(Path(__file__).parent / '.env')
openai.api_key = os.getenv('OPENAI_API_KEY')


# -------- chatbot --------
def run_chatbot():
    path_to_prompts = Path(__file__).parent / 'prompts'

    # set the chatbot system prompt
    with open(path_to_prompts / 'chatbot.txt', 'r') as file:
        chatbot_prompt = file.read()
    conversation_history = [{
        "role": "system",
        "content": chatbot_prompt
    }]

    # start with a welcome message
    with open(path_to_prompts / 'welcome.txt', 'r') as file:
        welcome_text = file.read()
    print(welcome_text)

    # main loop
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "-exit":
            print("Goodbye!")
            break

        # Append user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",  # Use "gpt-4" if you have access
                messages=conversation_history
            )

            # Get the assistant's reply
            assistant_reply = response['choices'][0]['message']['content']
            conversation_history.append({"role": "assistant", "content": assistant_reply})
            assistant_reply = json.loads(assistant_reply)

            print(f"Chatbot: {assistant_reply}")

            if assistant_reply.get('status', -1) != 0:
                print(ERRORS.get(assistant_reply.get('status', -1), "An error occurred."))
                continue

            rr = requests.post(
                url=f"http://localhost:8000/{assistant_reply.get('cmd', 'play')}",
                json={
                    "kind": assistant_reply.get('kind', 'music'),
                    "question": assistant_reply.get('question', '')
                }
            )
            print('Player response:', rr.status_code, rr.text)
            print()

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_chatbot()
