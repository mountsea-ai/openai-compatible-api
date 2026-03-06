/**
 * OpenAI Compatible API - Multi-Model Chat (Node.js)
 * Use GPT-4, Claude, Gemini with OpenAI SDK via Mountsea AI
 *
 * Documentation: https://docs.mountsea.ai/api-reference/chat/introduction
 * Platform: https://shanhaiapi.com/zh/
 */

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.MOUNTSEA_API_KEY || 'your-api-key',
  baseURL: 'https://api.mountsea.ai/v1'
});

async function chatWith(model, message) {
  const response = await client.chat.completions.create({
    model,
    messages: [{ role: 'user', content: message }]
  });
  return response.choices[0].message.content;
}

async function streamChat(model, message) {
  const stream = await client.chat.completions.create({
    model,
    messages: [{ role: 'user', content: message }],
    stream: true
  });
  for await (const chunk of stream) {
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  console.log();
}

(async () => {
  console.log('🤖 GPT-4:', await chatWith('gpt-4', 'Hello!'));
  console.log('🟣 Claude:', await chatWith('claude-3-opus', 'Hello!'));
  console.log('🔵 Gemini:', await chatWith('gemini-pro', 'Hello!'));
  console.log('\n📡 Streaming:');
  await streamChat('gpt-4', 'Tell me a joke');
  console.log('\n📘 Docs: https://docs.mountsea.ai/api-reference/chat/introduction');
})();

