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

zero_shot = """ Answer the question as it. Output format:
-- ZERO SHOT -- as heading then the answer below it."""
step_by_step = """ Answer the question step by step. Show the steps of reasoning. Output format:
-- STEP BY STEP -- as heading then the answer below it."""
while True:
    user_input=input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = chat.send_message(
        zero_shot + step_by_step + user_input,
        config=types.GenerateContentConfig(
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUTUT_TOKENS
        )
    )

    print(response.text)


