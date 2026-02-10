import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# from src.p1_chatbot.sys_prompt import SYSTEM_PROMPT
from src.p1_chatbot.tokens import MAX_OUTPUTUT_TOKENS, TEMPERATURE

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model="gemini-3-flash-preview")

prompt_classfier= """You are a helpful assistant that classifies the user's input into positive or negative
Examples:
I loved this movie. Great pacing and strong acting. → Positive
Not worth my time. The plot was confusing and boring. → Negative
Surprisingly good. I would watch it again. → Positive
Your Output should only be Positive or Negative. No intros or Outros. Just the classification.
"""

while True:
    user_input=input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = chat.send_message(
        prompt_classfier + user_input,
        config=types.GenerateContentConfig(
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUTUT_TOKENS
        )
    )

    print(response.text)


