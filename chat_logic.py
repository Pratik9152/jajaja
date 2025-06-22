
from backend.pdf_search import search_pdf
from backend.openrouter_fallback import smart_fallback

def get_response(query):
    answer = search_pdf(query)
    if answer:
        return f"📄 From Policy: {answer}"
    return smart_fallback(query)
