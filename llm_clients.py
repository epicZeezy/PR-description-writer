from llm_configs import *
from langchain_google_vertexai import ChatVertexAI
from langchain_community.chat_models import ChatOllama

def new_gemini_client(config=None):
    if config:
        return ChatVertexAI(**config)
    else:
        return ChatVertexAI(**GEMINI_PRO_STAGING_CONFIG)

def new_ollama_client(config=None):
    if config:
        return ChatOllama(**config)
    else:
        return ChatOllama(**OLLAMA_CONFIG)