from langgraph.graph import StateGraph
from typing import TypedDict, List

from agents.scout import scout_brand_mentions
from agents.judge import analyze_mention
from agents.writer import write_brand_reply

class AgentState(TypedDict):
    brand: str
    mentions: List[dict]
    analysis: dict
    reply: str

def scout_node(state: AgentState):
    try: 
        mentions = scout_brand_mentions(state["brand"])
        return {"mentions": mentions}
    except:
        print("[ERROR] Scout Node failed")
        return {"mentions": []}

def judge_node(state: AgentState):
    try:
        if not state.get("mentions"):
            raise ValueError("No mentions found")

        first_mention = state["mentions"][0]["text"]
        analysis = analyze_mention(first_mention).dict()
        return {"analysis": analysis}

    except Exception as e:
        print(f"[ERROR] Judge Node failed: {e}")
        return {
            "analysis": {
                "sentiment": "Unknown",
                "intent": "Error",
                "urgency_score": 0,
                "summary": "Analysis failed due to processing error"
            }
        }



def writer_node(state: AgentState):
    reply = write_brand_reply(state["analysis"])
    return {"reply": reply}

graph = StateGraph(AgentState)

graph.add_node("scout", scout_node)
graph.add_node("judge", judge_node)
graph.add_node("writer", writer_node)

graph.set_entry_point("scout")
graph.add_edge("scout", "judge")
graph.add_edge("judge", "writer")

agent_app = graph.compile()





