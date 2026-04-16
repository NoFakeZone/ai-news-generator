import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# 1. KONFIGURACJA - Tutaj podmieniasz klucz i model
os.environ["GOOGLE_API_KEY"] = "TWÓJ_KLUCZ_API"

# Definicja modelu
# max_retries automatycznie obsłuży błąd 429 (Too Many Requests)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    max_retries=6,  # Ile razy ma próbować ponownie przy błędzie limitu
)

def ask_llm(question):
    try:
        message = HumanMessage(content=question)
        response = llm.invoke([message])
        return response.content
    except Exception as e:
        return f"Błąd: {e}"

# Przykład użycia
pytanie = ""
print(ask_llm(pytanie))