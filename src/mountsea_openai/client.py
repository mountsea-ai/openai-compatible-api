"""
OpenAI-compatible Chat Client - GPT-4 / Claude / Gemini / DeepSeek

Docs: https://docs.mountsea.ai/api-reference/chat/introduction
Platform: https://shanhaiapi.com/zh/
"""
import requests


class ChatClient:
    """OpenAI-compatible multi-model chat client.

    Supports: GPT-4, GPT-4o, Claude 3, Gemini Pro, DeepSeek, etc.

    Example:
        >>> client = ChatClient("your-api-key")
        >>> print(client.chat("What is AI?", model="gpt-4"))
        >>> print(client.chat("Tell me a joke", model="claude-3-opus"))
    """

    def __init__(self, api_key: str, base_url: str = "https://api.mountsea.ai/v1", timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self._s = requests.Session()
        self._s.headers.update({"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})

    def chat(self, message: str, model: str = "gpt-4", system: str = None, **kwargs) -> str:
        """Send a message and get a reply."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": message})
        resp = self._s.post(f"{self.base_url}/chat/completions",
                            json={"model": model, "messages": messages, **kwargs},
                            timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    def chat_raw(self, messages: list, model: str = "gpt-4", **kwargs) -> dict:
        """Send messages and return full API response."""
        resp = self._s.post(f"{self.base_url}/chat/completions",
                            json={"model": model, "messages": messages, **kwargs},
                            timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def stream(self, message: str, model: str = "gpt-4", **kwargs):
        """Stream a chat response. Yields content chunks."""
        messages = [{"role": "user", "content": message}]
        resp = self._s.post(f"{self.base_url}/chat/completions",
                            json={"model": model, "messages": messages, "stream": True, **kwargs},
                            timeout=self.timeout, stream=True)
        resp.raise_for_status()
        for line in resp.iter_lines():
            if line:
                text = line.decode("utf-8")
                if text.startswith("data: ") and text != "data: [DONE]":
                    import json
                    chunk = json.loads(text[6:])
                    content = chunk.get("choices", [{}])[0].get("delta", {}).get("content", "")
                    if content:
                        yield content

