# Multi-Agent Brand Reputation Monitor

A multi-agent AI system that monitors brand mentions, analyzes sentiment and intent, and generates brand-safe response drafts using Retrieval-Augmented Generation (RAG) and autonomous agents.

Currently demonstrated with a single brand-specific knowledge base (Mamaearth).
For other brands, the system executes the full multi-agent pipeline but intentionally falls back to safe default handling when brand knowledge is unavailable. This project focuses on showcasing scalable architecture, agent orchestration, and RAG integration rather than multi-brand data coverage.


---

## Features

- **Brand Mention Discovery**
  - Simulates real-world brand mentions from online platforms
- **Multi-Agent Architecture**
  - Scout Agent: detects brand mentions
  - Analyst Agent: sentiment, intent & urgency analysis
  - Writer Agent: drafts brand-safe replies
- **Brand Knowledge via RAG**
  - Uses brand guidelines ingested into a vector database
- **Safe Fallback Handling**
  - Gracefully handles missing brand knowledge without system failure
- **Interactive UI**
  - Built using Streamlit for real-time testing

---

## System Architecture
```
User Input (Brand)
↓
Scout Agent (Find Mention)
↓
Analyst Agent (Sentiment + Intent)
↓
Writer Agent
├── Uses Brand Guidelines (if available)
└── Uses Safe Generic Reply (fallback)
↓
Streamlit UI Output
```
