


from langchain_community.chat_models.ollama import ChatOllama
from rag.query import get_brand_rules

llm = ChatOllama(model="llama3", temperature=0.2)

def write_brand_reply(analysis: dict):
    brand_context = get_brand_rules(
        f"How should the brand respond to a {analysis['intent']} with {analysis['sentiment']} sentiment?"
    )

    prompt = f"""
SYSTEM:
You are a professional Brand Response Generator.
You must strictly follow brand rules.

BRAND GUIDELINES:
{brand_context}

CUSTOMER ISSUE SUMMARY:
{analysis['summary']}

RULES:
- Be empathetic
- Never blame the customer
- Offer next steps if complaint
- Keep response under 60 words

OUTPUT:
Return ONLY the final reply text.
"""

    response = llm.invoke(prompt)
    return response.content.strip()
