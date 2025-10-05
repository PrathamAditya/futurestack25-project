import React from "react";

export default function EvaluationResults({ results }) {
  if (!results || !results.results) return null;

  return (
    <div className="fade-in">
      <h3>Evaluation Results</h3>

      {results.results.map((item, idx) => (
        <div key={idx} className="question-card">
          <h5>Q{idx + 1}</h5>
          <p>
            <strong>Question:</strong> {item.question}
          </p>
          <p>
            <strong>Your Answer:</strong> {item.answer}
          </p>
          <p className="result-score">Score: {item.score} / 5</p>
          <div className="feedback-box">{item.feedback}</div>
        </div>
      ))}

      <div className="mt-4 p-3 rounded" style={{ backgroundColor: "#222" }}>
        <h4>
          Overall Score:{" "}
          <span className="result-score">
            {results.overall_score?.toFixed(1)}
          </span>{" "}
          / 5
        </h4>
        <p className="mt-2">{results.summary_feedback}</p>
      </div>
    </div>
  );
}
