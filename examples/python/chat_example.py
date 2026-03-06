"""
OpenAI Compatible API - Chat Example
Use any OpenAI SDK to access GPT-4, Claude, Gemini and more

Documentation: https://docs.mountsea.ai/api-reference/chat/introduction
Platform: https://shanhaiapi.com/zh/
"""

from openai import OpenAI
import os

API_KEY = os.environ.get("MOUNTSEA_API_KEY", "your-api-key")

# Just change the base_url to Mountsea AI
client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.mountsea.ai/v1"
)


def chat_with_gpt4(message: str) -> str:
    """Chat using GPT-4."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].message.content


def chat_with_claude(message: str) -> str:
    """Chat using Claude via OpenAI-compatible API."""
    response = client.chat.completions.create(
        model="claude-3-opus",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content


def chat_with_gemini(message: str) -> str:
    """Chat using Gemini via OpenAI-compatible API."""
    response = client.chat.completions.create(
        model="gemini-pro",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    return response.choices[0].message.content


def streaming_chat(message: str, model: str = "gpt-4"):
    """Streaming chat example."""
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
        stream=True
    )
    
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content
    
    print()
    return full_response


if __name__ == "__main__":
    # GPT-4 Example
    print("🤖 GPT-4:")
    print(chat_with_gpt4("What is artificial intelligence?"))
    print()
    
    # Claude Example
    print("🟣 Claude:")
    print(chat_with_claude("Write a haiku about coding."))
    print()
    
    # Gemini Example
    print("🔵 Gemini:")
    print(chat_with_gemini("Explain machine learning in one sentence."))
    print()
    
    # Streaming Example
    print("📡 Streaming (GPT-4):")
    streaming_chat("Tell me a short joke about programming.")
    
    print("\n🔗 Documentation: https://docs.mountsea.ai/api-reference/chat/introduction")
    print("🏠 Platform: https://shanhaiapi.com/zh/")

