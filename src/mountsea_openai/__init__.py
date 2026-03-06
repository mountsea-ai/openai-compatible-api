"""
Mountsea OpenAI-compatible SDK - GPT-4, Claude, Gemini with one API

    >>> from mountsea_openai import ChatClient
    >>> client = ChatClient("your-api-key")
    >>> print(client.chat("Hello!", model="gpt-4"))

Docs: https://docs.mountsea.ai/api-reference/chat/introduction
"""
from .client import ChatClient
__version__ = "1.0.0"
__all__ = ["ChatClient"]

