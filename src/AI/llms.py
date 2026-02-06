from langchain_google_genai import ChatGoogleGenerativeAI
from django.conf import settings


def get_gemini_api_key():
    # ApiKey.objects.get(provider='gemini', org='CFE)
    return settings.GEMINI_API_KEY


def get_gemini_model(model="gemini-2.5-flash"):
    if model is None:
        model = "gemini-2.5-flash"
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=get_gemini_api_key(),
        # other params...
    )