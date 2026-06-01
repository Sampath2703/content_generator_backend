from fastapi import FastAPI
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()
app = FastAPI()



cilent = Groq(
    api_key=os.getenv("api_key")
)

@app.post("/generate")
def generate_content(topic:str,technology:str,content_type:str,tone:str):
    prompt = f"""
    You are a professional content writer.

    Generate a {content_type} based on the following details:

    Topic: {topic}
    Technology: {technology}
    Tone: {tone}

    Instructions:
    - Write high-quality and engaging content.
    - Use clear and professional language.
    - Make the content relevant to the technology mentioned.
    - Follow the requested tone consistently.
    - Include a strong introduction.
    - Include useful insights, examples, and benefits where appropriate.
    - End with a strong conclusion or call-to-action.
    - Return only the content.
"""
    response = cilent.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = [
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return {
        "content":response.choices[0].message.content
    }