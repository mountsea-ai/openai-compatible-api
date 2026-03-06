# 🔌 OpenAI Compatible API - Multi-Model AI API Gateway

[English](#english) | [中文](#中文)

> A unified OpenAI-compatible API gateway that provides access to GPT-4, Claude, Gemini, and more. Use your favorite OpenAI SDK to access all top AI models at a fraction of the cost.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![API Status](https://img.shields.io/badge/API-Online-green.svg)](https://shanhaiapi.com/zh/)
[![Documentation](https://img.shields.io/badge/Docs-Available-blue.svg)](https://docs.mountsea.ai/api-reference/chat/introduction)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-412991.svg)](https://docs.mountsea.ai/api-reference/chat/introduction)

---

<a name="english"></a>

## ✨ Why Use This?

- 🔄 **One API, All Models** – Access GPT-4, Claude, Gemini with a single API key
- 💰 **Save Money** – Much cheaper than using each provider directly
- 🔌 **Drop-in Replacement** – Works with existing OpenAI SDK code, zero changes needed
- 🌐 **Multi-Protocol** – OpenAI, Anthropic (Claude), Google Gemini native protocols
- ⚡ **Fast & Reliable** – Optimized infrastructure with high availability
- 🛡️ **No Rate Limits** – Enterprise-grade capacity

## 🚀 Quick Start

### Get Your API Key

1. Visit [Mountsea AI Platform](https://shanhaiapi.com/zh/)
2. Sign up and get your API key
3. Replace `base_url` in your code – done!

### Install SDK

```bash
# Python
pip install mountsea-openai

# Node.js
npm install mountsea-openai
```

### SDK Quick Start

```python
from mountsea_openai import ChatClient

client = ChatClient("your-api-key")
print(client.chat("Hello!", model="gpt-4"))
print(client.chat("Tell me a joke", model="claude-3-opus"))
print(client.chat("What is AI?", model="gemini-pro"))
```

```javascript
const { ChatClient } = require('mountsea-openai');
const client = new ChatClient('your-api-key');
console.log(await client.chat('Hello!', 'gpt-4'));
```

### Python (OpenAI SDK)

```python
from openai import OpenAI

# Just change api_key and base_url, everything else stays the same!
client = OpenAI(
    api_key="your-mountsea-api-key",
    base_url="https://api.mountsea.ai/v1"
)

# Use GPT-4
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    temperature=0.7,
    max_tokens=1000
)

print(response.choices[0].message.content)
```

### Use Claude via OpenAI SDK

```python
# Access Claude through the same OpenAI-compatible interface
response = client.chat.completions.create(
    model="claude-3-opus",
    messages=[
        {"role": "user", "content": "Write a haiku about programming."}
    ]
)

print(response.choices[0].message.content)
```

### Use Gemini via OpenAI SDK

```python
# Access Gemini through the same interface
response = client.chat.completions.create(
    model="gemini-pro",
    messages=[
        {"role": "user", "content": "What are the latest trends in AI?"}
    ]
)

print(response.choices[0].message.content)
```

### Streaming

```python
# Streaming responses
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Tell me a story about a robot."}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Node.js (OpenAI SDK)

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.MOUNTSEA_API_KEY || 'your-api-key',
  baseURL: 'https://api.mountsea.ai/v1'
});

// GPT-4
const response = await client.chat.completions.create({
  model: 'gpt-4',
  messages: [
    { role: 'system', content: 'You are a helpful assistant.' },
    { role: 'user', content: 'Hello!' }
  ]
});

console.log(response.choices[0].message.content);

// Streaming
const stream = await client.chat.completions.create({
  model: 'gpt-4',
  messages: [{ role: 'user', content: 'Tell me a joke' }],
  stream: true
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || '');
}
```

### Anthropic SDK (Native Claude Protocol)

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="your-mountsea-api-key",
    base_url="https://api.mountsea.ai"
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

print(message.content[0].text)
```

### cURL

```bash
# OpenAI-compatible endpoint
curl -X POST https://api.mountsea.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "Hello!"}
    ],
    "temperature": 0.7
  }'
```

## 📖 Supported Models

### OpenAI Models
| Model | Description |
|-------|-------------|
| `gpt-4` | Most capable GPT model |
| `gpt-4-turbo` | Faster GPT-4 variant |
| `gpt-3.5-turbo` | Fast and affordable |

### Anthropic Models
| Model | Description |
|-------|-------------|
| `claude-3-opus` | Most capable Claude model |
| `claude-3-sonnet` | Balanced performance |
| `claude-3-haiku` | Fast and efficient |

### Google Models
| Model | Description |
|-------|-------------|
| `gemini-pro` | Versatile Gemini model |
| `gemini-pro-vision` | Multimodal capabilities |
| `gemini-ultra` | Most powerful Gemini |

## 🔌 Compatible Applications

Works seamlessly with:

- ✅ **OpenAI Python SDK** – Drop-in replacement
- ✅ **OpenAI Node.js SDK** – Drop-in replacement
- ✅ **Anthropic SDK** – Native support
- ✅ **Cherry Studio** – Full compatibility
- ✅ **Cursor** – AI-powered code editor
- ✅ **Claude Code** – Anthropic's coding tool
- ✅ **LangChain** – AI framework
- ✅ **LlamaIndex** – Data framework
- ✅ **AutoGPT** – Autonomous agents
- ✅ Any OpenAI-compatible application

## 🔧 Configuration for Popular Tools

### Cursor

```json
{
  "openai.apiKey": "your-mountsea-api-key",
  "openai.baseUrl": "https://api.mountsea.ai/v1"
}
```

### Cherry Studio

```
API Base URL: https://api.mountsea.ai/v1
API Key: your-mountsea-api-key
```

### LangChain

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4",
    openai_api_key="your-mountsea-api-key",
    openai_api_base="https://api.mountsea.ai/v1"
)

response = llm.invoke("Hello!")
print(response.content)
```

## 💰 Pricing

| Package | Credits | Price |
|---------|---------|-------|
| Starter | 10,000 | ¥100 |
| Basic | 50,000 | ¥500 |
| Pro | 200,000 | ¥2,000 |
| Business | 500,000 | ¥4,500 (10% OFF) |
| Enterprise | 1,000,000 | ¥8,000 (20% OFF) |

👉 [View Full Pricing](https://shanhaiapi.com/zh/)

## 📚 Documentation

- 📘 [Chat API Documentation](https://docs.mountsea.ai/api-reference/chat/introduction)
- 📘 [Gemini API Documentation](https://docs.mountsea.ai/api-reference/gemini/introduction)
- 🏠 [Mountsea AI Platform](https://shanhaiapi.com/zh/)

## 🔗 Related Projects

- [Suno API](https://github.com/mountsea-ai/suno-api) - AI Music Generation API
- [Sora API](https://github.com/mountsea-ai/sora-api) - AI Video Generation API
- [Veo API](https://github.com/mountsea-ai/veo-api) - Google Veo Video Generation API
- [Gemini API](https://github.com/mountsea-ai/gemini-api) - Google Gemini API
- [Awesome AI API](https://github.com/mountsea-ai/awesome-ai-api) - Curated list of AI APIs

---

<a name="中文"></a>

## 🇨🇳 中文文档

# 🔌 OpenAI 兼容 API - 多模型 AI API 网关

> 统一的 OpenAI 兼容 API 网关，提供 GPT-4、Claude、Gemini 等模型访问。使用你熟悉的 OpenAI SDK 以极低价格访问所有顶级 AI 模型。

## ✨ 为什么选择我们？

- 🔄 **一个 API，所有模型** – 用一个 API 密钥访问 GPT-4、Claude、Gemini
- 💰 **省钱** – 比直接使用各提供商便宜很多
- 🔌 **即插即用** – 兼容现有 OpenAI SDK 代码，无需修改
- 🌐 **多协议** – 支持 OpenAI、Anthropic（Claude）、Google Gemini 原生协议
- ⚡ **快速可靠** – 优化的基础设施，高可用性

## 🚀 快速开始

### 获取 API 密钥

1. 访问 [Mountsea AI 平台](https://shanhaiapi.com/zh/)
2. 注册账号并获取 API 密钥
3. 替换代码中的 `base_url` – 搞定！

### Python 示例

```python
from openai import OpenAI

# 只需更改 api_key 和 base_url，其他代码完全不变！
client = OpenAI(
    api_key="your-mountsea-api-key",
    base_url="https://api.mountsea.ai/v1"
)

# 使用 GPT-4
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "你是一个有用的助手。"},
        {"role": "user", "content": "用简单的话解释量子计算。"}
    ]
)

print(response.choices[0].message.content)
```

### 支持的客户端

- ✅ OpenAI Python/Node.js SDK
- ✅ Anthropic SDK
- ✅ Cherry Studio
- ✅ Cursor
- ✅ Claude Code
- ✅ LangChain
- ✅ 任何 OpenAI 兼容应用

## 📚 文档

- 📘 [Chat API 完整文档](https://docs.mountsea.ai/api-reference/chat/introduction)
- 📘 [Gemini API 完整文档](https://docs.mountsea.ai/api-reference/gemini/introduction)
- 🏠 [Mountsea AI 官网](https://shanhaiapi.com/zh/)

## ⭐ Star History

如果这个项目对你有帮助，请给我们一个 Star ⭐

## 📄 License

[MIT License](LICENSE)

---

**Powered by [Mountsea AI](https://shanhaiapi.com/zh/) – 全球顶级 AI API 一体化平台**

<!-- Auto-updated by CI -->
> Last API Check: 2026-03-06 | Status: online
