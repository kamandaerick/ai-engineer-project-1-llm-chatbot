import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# from src.p1_chatbot.sys_prompt import SYSTEM_PROMPT
from src.p1_chatbot.tokens import MAX_OUTPUTUT_TOKENS, TEMPERATURE

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)
chat = client.chats.create(model="gemini-2.5-flash")


while True:
    user_input=input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    if "/cot" in user_input.lower():
        user_input += "Explain your reasoning step-by-step, then give the final answer.\n\n Start the answer with '[mode] CoT enabled for next turn' and end with '[mode] CoT disabled'"

    response = chat.send_message(
        user_input,
        config=types.GenerateContentConfig(
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUTUT_TOKENS
        )
    )

    print(response.text)


