import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from rich import print
import streamlit as st

# 1. exercise

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(
        api_key=gemini_api_key
    )


with open("./image/photo.jpg", "rb") as f:
    image = f.read()

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        types.Part.from_bytes(data=image, mime_type="image/png"),
        "THis is me. What popular place I visited? Answer in Lithuanian language.",
    ],
    
)

print(response.text)




