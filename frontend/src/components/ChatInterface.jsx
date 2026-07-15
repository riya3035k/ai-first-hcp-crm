import { useState } from "react";
import { sendChatMessage } from "../services/api";

function ChatInterface() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMessage = message;

    setMessages((prev) => [
      ...prev,
      { role: "user", text: userMessage },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const response = await sendChatMessage(userMessage);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: response.data.response,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Unable to process your request.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>AI HCP Assistant</h2>

      <p>
        Manage HCP interactions using natural language.
      </p>

      <div>
        {messages.map((item, index) => (
          <div key={index}>
            <strong>
              {item.role === "user" ? "You: " : "AI Assistant: "}
            </strong>

            <span>{item.text}</span>
          </div>
        ))}

        {loading && <p>AI Assistant is thinking...</p>}
      </div>

      <textarea
        placeholder="Example: Search for HCP named Dr. Sharma"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <br />

      <button onClick={handleSend} disabled={loading}>
        Send
      </button>
    </div>
  );
}

export default ChatInterface;