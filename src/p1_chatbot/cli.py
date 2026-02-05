import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from .sys_prompt import SYSTEM_PROMPT
from .tokens import MAX_OUTPUTUT_TOKENS, TEMPERATURE

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=[SYSTEM_PROMPT, user_input],
        config=types.GenerateContentConfig(
        temperature=TEMPERATURE,
        max_output_tokens=MAX_OUTPUTUT_TOKENS
        )
    )

    print(response.text)


