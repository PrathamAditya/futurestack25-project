import React from "react";

export default function EvaluationResults({ results }) {
  if (!results) return null;

  return (
    <div className="card mt-4">
      <h2>Step 3: Evaluation Results</h2>

      {results.results.map((item, idx) => (
        <div key={idx} className="mb-3">
          <strong>
            Q{idx + 1}: {item.question}
          </strong>
          <p>
            <em>Your Answer:</em> {item.answer}
          </p>
          <p>
            <strong>Score:</strong> {item.score} / 5
          </p>
          <p>
            <strong>Feedback:</strong> {item.feedback}
          </p>
          <hr />
        </div>
      ))}

      <div className="mt-3">
        <h4>Overall Score: {results.overall_score} / 5</h4>
        <p>{results.summary_feedback}</p>
      </div>
    </div>
  );
}
