
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from pydantic import BaseModel, Field

llm = ChatOllama(model="llama3", temperature=0)

class Analysis(BaseModel):
    sentiment: str = Field(description="Positive, Negative, or Neutral")
    intent: str = Field(description="Complaint, Compliment, or Inquiry")
    urgency_score: int = Field(description="1 (low) to 10 (critical)")
    summary: str

def analyze_mention(text: str) -> Analysis:
    prompt = f"""
SYSTEM: You are a cold, precise Data Extraction API.
INPUT: "{text}"

TASK:
Categorize the brand mention.

JSON STRUCTURE:
{{
  "sentiment": "Positive" | "Negative" | "Neutral",
  "intent": "Complaint" | "Compliment" | "Inquiry",
  "urgency_score": 1-10,
  "summary": "string"
}}

RULES:
- Output ONLY valid JSON
- No explanation
- No markdown
"""

    response = llm.invoke(prompt)
    return Analysis.model_validate_json(response.content)
