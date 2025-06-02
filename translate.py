import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_to_uzbek(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Quyidagi matnni o‘zbek tiliga tarjima qil: {text}"
            }]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Tarjima qilishda xatolik: {e}"
      
