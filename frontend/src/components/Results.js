import React from "react";

export default function Results({ result }) {
  if (!result) return null;

  return (
    <div className="card mt-4">
      <h2>Step 1: Analysis Results</h2>

      <div className="mt-3">
        <h5>AI Feedback</h5>
        <pre style={{ whiteSpace: "pre-wrap" }}>
          {JSON.stringify(result.ai_feedback, null, 2)}
        </pre>
      </div>

      <div className="mt-3">
        <h5>Skill Match</h5>
        <p>{result.comparison.skill_match}</p>

        <h5>Experience Match</h5>
        <p>{result.comparison.experience_match}</p>

        <h5>Project Alignment</h5>
        <p>{result.comparison.project_alignment}</p>
      </div>
    </div>
  );
}
