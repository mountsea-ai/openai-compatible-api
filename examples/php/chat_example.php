<?php
/**
 * OpenAI Compatible API - Multi-Model Chat (PHP)
 * Use GPT-4, Claude, Gemini via Mountsea AI
 *
 * Documentation: https://docs.mountsea.ai/api-reference/chat/introduction
 * Platform: https://shanhaiapi.com/zh/
 */

$API_KEY = getenv('MOUNTSEA_API_KEY') ?: 'your-api-key';
$BASE_URL = 'https://api.mountsea.ai/v1';

function chat(string $model, string $message): string
{
    global $API_KEY, $BASE_URL;
    $ch = curl_init("$BASE_URL/chat/completions");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => ["Authorization: Bearer $API_KEY", 'Content-Type: application/json'],
        CURLOPT_POSTFIELDS => json_encode([
            'model' => $model,
            'messages' => [['role' => 'user', 'content' => $message]],
        ]),
    ]);
    $resp = curl_exec($ch);
    curl_close($ch);
    $data = json_decode($resp, true);
    return $data['choices'][0]['message']['content'] ?? 'No response';
}

echo "🤖 GPT-4: " . chat('gpt-4', 'Hello!') . "\n";
echo "🟣 Claude: " . chat('claude-3-opus', 'Hello!') . "\n";
echo "🔵 Gemini: " . chat('gemini-pro', 'Hello!') . "\n";
echo "\n📘 Docs: https://docs.mountsea.ai/api-reference/chat/introduction\n";

