#!/bin/bash
# OpenAI Compatible API - Multi-Model Chat (cURL)
# GPT-4, Claude, Gemini - all with one API
#
# Documentation: https://docs.mountsea.ai/api-reference/chat/introduction
# Platform: https://shanhaiapi.com/zh/

API_KEY="${MOUNTSEA_API_KEY:-your-api-key}"
BASE_URL="https://api.mountsea.ai/v1"

# GPT-4
echo "🤖 GPT-4:"
curl -s -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-4","messages":[{"role":"user","content":"Hello!"}]}'

# Claude
echo -e "\n🟣 Claude:"
curl -s -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"model":"claude-3-opus","messages":[{"role":"user","content":"Hello!"}]}'

# Gemini
echo -e "\n🔵 Gemini:"
curl -s -X POST "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"model":"gemini-pro","messages":[{"role":"user","content":"Hello!"}]}'

echo -e "\n📘 Docs: https://docs.mountsea.ai/api-reference/chat/introduction"

