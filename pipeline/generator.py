from llm_clients.openrouter_client import get_response

def generate_responses(prompt):
    return {
        "A": get_response("openai/gpt-4o-mini", prompt),
        "B": get_response("google/gemini-3-flash-preview", prompt)
    }