
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "data/vector_store"

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectordb = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

def get_brand_rules(query: str) -> str:
    docs = vectordb.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

DB_DIR = "data/vector_store"

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectordb = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

def get_brand_rules(query: str) -> str:
    docs = vectordb.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])
