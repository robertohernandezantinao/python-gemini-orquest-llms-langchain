import google.generativeai as genai
from my_keys import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

for modelo in genai.list_models():
    if "generateContent" in modelo.supported_generation_methods:
        print(modelo.name)