/**
 * Mountsea OpenAI-compatible SDK - GPT-4, Claude, Gemini in one API
 * @example
 * const { ChatClient } = require('mountsea-openai');
 * const client = new ChatClient('your-api-key');
 * const reply = await client.chat('Hello!', 'gpt-4');
 *
 * Docs: https://docs.mountsea.ai/api-reference/chat/introduction
 */
const https = require('https');
const http = require('http');
const { URL } = require('url');

class ChatClient {
  constructor(apiKey, options = {}) {
    this.apiKey = apiKey;
    this.baseUrl = (options.baseUrl || 'https://api.mountsea.ai/v1').replace(/\/$/, '');
    this.timeout = options.timeout || 60000;
  }

  async chat(message, model = 'gpt-4', options = {}) {
    const messages = [];
    if (options.system) messages.push({ role: 'system', content: options.system });
    messages.push({ role: 'user', content: message });
    const resp = await this._post('/chat/completions', { model, messages, ...options });
    return resp.choices[0].message.content;
  }

  async chatRaw(messages, model = 'gpt-4', options = {}) {
    return this._post('/chat/completions', { model, messages, ...options });
  }

  _post(p, b) {
    return new Promise((resolve, reject) => {
      const url = new URL(this.baseUrl + p);
      const mod = url.protocol === 'https:' ? https : http;
      const req = mod.request({
        method: 'POST', hostname: url.hostname, port: url.port, path: url.pathname + url.search,
        headers: { 'Authorization': `Bearer ${this.apiKey}`, 'Content-Type': 'application/json' },
        timeout: this.timeout,
      }, res => { let d = ''; res.on('data', c => d += c); res.on('end', () => { try { resolve(JSON.parse(d)); } catch { reject(new Error(d)); } }); });
      req.on('error', reject);
      if (b) req.write(JSON.stringify(b));
      req.end();
    });
  }
}

module.exports = { ChatClient };

