/**
 * OpenAI Compatible API - Multi-Model Chat (Java)
 * Use GPT-4, Claude, Gemini with one API via Mountsea AI
 *
 * Documentation: https://docs.mountsea.ai/api-reference/chat/introduction
 * Platform: https://shanhaiapi.com/zh/
 */

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ChatApiExample {

    private static final String API_KEY = System.getenv("MOUNTSEA_API_KEY") != null
            ? System.getenv("MOUNTSEA_API_KEY") : "your-api-key";
    private static final String BASE_URL = "https://api.mountsea.ai/v1";

    static String chat(HttpClient client, String model, String message) throws Exception {
        String body = String.format("""
                {"model": "%s", "messages": [{"role": "user", "content": "%s"}]}
                """, model, message);
        HttpRequest req = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/chat/completions"))
                .header("Authorization", "Bearer " + API_KEY)
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();
        return client.send(req, HttpResponse.BodyHandlers.ofString()).body();
    }

    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        System.out.println("🤖 GPT-4: " + chat(client, "gpt-4", "Hello!"));
        System.out.println("🟣 Claude: " + chat(client, "claude-3-opus", "Hello!"));
        System.out.println("🔵 Gemini: " + chat(client, "gemini-pro", "Hello!"));
        System.out.println("\n📘 Docs: https://docs.mountsea.ai/api-reference/chat/introduction");
    }
}

