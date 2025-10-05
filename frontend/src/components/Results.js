import React from "react";
import ReactMarkdown from "react-markdown";

export default function Results({ result }) {
  if (!result) return null;

  const { ai_feedback } = result;

  return (
    <div className="fade-in">
      <div className="mb-3">
        <h5>AI Feedback</h5>
        <div className="feedback-box">
          <ReactMarkdown>
            {ai_feedback || "No feedback available"}
          </ReactMarkdown>
        </div>
      </div>
    </div>
  );
}
