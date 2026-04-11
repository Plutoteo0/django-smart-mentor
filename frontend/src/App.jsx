import { useState } from "react";
import axios from "axios";
import ReactMardown from "react-markdown";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { vscDarkPlus } from "react-syntax-highlighter/dist/esm/styles/prism";

function App() {
  const [count, setCount] = useState(0);

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const ask_mentor = async () => {
    if (!question) return;
    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/ask", {
        question: question,
      });
      setAnswer(res.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Something went wrong. Please try again later.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div
        style={{
          maxWidth: "900px",
          margin: "40px auto",
          padding: "20px",
          fontFamily: "Segoe UI, Tahoma, Geneva, Verdana, sans-serif",
          color: "#333",
        }}
      >
        <h1 style={{ textAlign: "center", color: "#2c3e50" }}>
          Django Smart Mentor
        </h1>
        <p style={{ textAlign: "center", color: "#7f8c8d" }}>
          Powered by Llama 3.2
        </p>

        <div style={{ marginBottom: "20px " }}>
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Zadaj pytanie o Django..."
            style={{
              width: "100%",
              height: "120px",
              padding: "15px",
              borderRadius: "10px",
              border: "1px solid #ccc",
              fontSize: "16px",
              boxSizing: "border-box",
            }}
          ></textarea>
          <button
            onClick={ask_mentor}
            disabled={loading}
            style={{
              width: "100%",
              padding: "12px",
              marginTop: "10px",
              backgroundColor: loading ? "#bdc3c7" : "#3498db",
              color: "white",
              border: "none",
              borderRadius: "8px",
              fontSize: "18px",
              cursor: "pointer",
              fontWeight: "bold",
            }}
          >
            {loading ? "Mozg pracuje..." : "Zapytaj Mentora"}
          </button>
        </div>

        {answer && (
          <div
            style={{
              backgroundColor: "#fff",
              padding: "25px",
              borderRadius: "12px",
              border: "1px solid #e0e0e0",
              boxShadow: "0 4px 6px rgba(0,0,0,0.1)",
              lineHeight: "1.6",
            }}
          >
            <h3 style={{ marginTop: "0", color: "#2980b9" }}>Odpowiedz:</h3>
            <ReactMardown
              children={answer}
              components={{
                code({ node, inline, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || "");
                  return !inline && match ? (
                    <SyntaxHighlighter
                      children={String(children).replace(/\n$/, "")}
                      style={vscDarkPlus}
                      language={match[1]}
                      PreTag="div"
                      {...props}
                    />
                  ) : (
                    <code className={className} {...props}>
                      {children}
                    </code>
                  );
                },
              }}
            ></ReactMardown>
          </div>
        )}
      </div>
    </>
  );
}

export default App;
