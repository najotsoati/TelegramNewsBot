import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def translate_to_uzbek(text: str) -> str:
    messages = [
        {"role": "system", "content": "Siz tarjimonsiz. Matnni o'zbek tiliga tarjima qiling."},
        {"role": "user", "content": text},
    ]
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1000,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()
