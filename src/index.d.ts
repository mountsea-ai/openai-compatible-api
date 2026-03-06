export interface ChatClientOptions { baseUrl?: string; timeout?: number; }
export interface ChatOptions { system?: string; temperature?: number; max_tokens?: number; [key: string]: any; }

export declare class ChatClient {
  constructor(apiKey: string, options?: ChatClientOptions);
  chat(message: string, model?: string, options?: ChatOptions): Promise<string>;
  chatRaw(messages: Array<{role: string; content: string}>, model?: string, options?: ChatOptions): Promise<any>;
}

