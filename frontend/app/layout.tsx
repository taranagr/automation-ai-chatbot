import "./globals.css";

export const metadata = {
  title: "AI Chatbot",
  description: "Claude 3.5 Sonnet chatbot"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="min-h-screen bg-background text-foreground">
        {children}
      </body>
    </html>
  );
}
