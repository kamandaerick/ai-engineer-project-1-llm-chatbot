import os
from dotenv import load_dotenv
from google import genai
from prompts import SYSTEM_PROMPT as system_prompt

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=[system_prompt, user_input]
    )

    print(response.text)


