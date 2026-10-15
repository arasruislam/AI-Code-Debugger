# File: services/gemini_service.py
from typing import Optional
from PIL import Image
import google.generativeai as genai

from config.settings import MODEL_NAME
from utils.prompts import build_debug_prompt


def analyze_code_error(
    api_key: str,
    response_type: str,
    code_input: str = "",
    image: Optional[Image.Image] = None,
) -> str:
    """Sends the prompt, code, and/or error screenshot to Gemini API and returns the Markdown response."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(MODEL_NAME)

    prompt_text = build_debug_prompt(response_type, code_input)
    contents = [prompt_text]

    if image is not None:
        contents.append(image)

    response = model.generate_content(contents)
    return response.text
