import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)

# while True:
#     user_input=input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Exiting the chat. Goodbye!")
#         break
#     response = client.models.generate_content(
#         model="gemini-3-flash-preview", contents=user_input
#     )

#     print(response.text)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break

    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=user_input,
    )

    for chunk in response:
        print(chunk.text, end="", flush=True)

