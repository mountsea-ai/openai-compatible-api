// OpenAI Compatible API - Multi-Model Chat (Go)
// Use GPT-4, Claude, Gemini via Mountsea AI
//
// Documentation: https://docs.mountsea.ai/api-reference/chat/introduction
// Platform: https://shanhaiapi.com/zh/

package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

const baseURL = "https://api.mountsea.ai/v1"

var apiKey = getEnv("MOUNTSEA_API_KEY", "your-api-key")

func getEnv(key, fb string) string {
	if v := os.Getenv(key); v != "" {
		return v
	}
	return fb
}

func chat(model, message string) (string, error) {
	body, _ := json.Marshal(map[string]interface{}{
		"model": model,
		"messages": []map[string]string{
			{"role": "user", "content": message},
		},
	})
	req, _ := http.NewRequest("POST", baseURL+"/chat/completions", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")
	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()
	data, _ := io.ReadAll(resp.Body)
	var result map[string]interface{}
	json.Unmarshal(data, &result)
	choices := result["choices"].([]interface{})
	msg := choices[0].(map[string]interface{})["message"].(map[string]interface{})
	return msg["content"].(string), nil
}

func main() {
	models := map[string]string{"GPT-4": "gpt-4", "Claude": "claude-3-opus", "Gemini": "gemini-pro"}
	for name, model := range models {
		answer, err := chat(model, "Hello, who are you?")
		if err != nil {
			fmt.Printf("%s Error: %v\n", name, err)
			continue
		}
		fmt.Printf("🤖 %s: %s\n\n", name, answer)
	}
	fmt.Println("📘 Docs: https://docs.mountsea.ai/api-reference/chat/introduction")
}

