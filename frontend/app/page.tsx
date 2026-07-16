"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

type Message = { role: "user" | "assistant"; content: string };

export default function HomePage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  async function sendMessage() {
    if (!input.trim()) return;
    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch(process.env.NEXT_PUBLIC_API_URL + "/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMessage.content })
      });

      const data = await res.json();
      setMessages((prev) => [...prev, { role: "assistant", content: data.content }]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="flex min-h-screen items-center justify-center bg-background">
      <div className="w-full max-w-2xl border rounded-lg p-4 space-y-4 bg-white">
        <h1 className="text-xl font-semibold">Claude 3.5 Sonnet Chatbot</h1>
        <div className="h-80 overflow-y-auto border rounded-md p-3 space-y-2 text-sm bg-neutral-50">
          {messages.map((m, i) => (
            <div key={i} className={m.role === "user" ? "text-right" : "text-left"}>
              <span className="font-semibold">{m.role === "user" ? "You" : "Assistant"}: </span>
              <span>{m.content}</span>
            </div>
          ))}
          {loading && <div className="italic text-neutral-500">Assistant is typing…</div>}
        </div>
        <div className="flex gap-2">
          <Input
            placeholder="Ask me anything…"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <Button onClick={sendMessage} disabled={loading}>
            Send
          </Button>
        </div>
      </div>
    </main>
  );
}
