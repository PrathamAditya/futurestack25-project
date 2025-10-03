import React from "react";
import ReactMarkdown from "react-markdown";

export default function Results({ result }) {
  if (!result) return null;

  const { ai_feedback, comparison } = result;

  const renderProgressBar = (label, value, color) => (
    <div className="mb-3">
      <div className="d-flex justify-content-between">
        <strong>{label}</strong>
        <span>{value}%</span>
      </div>
      <div className="progress" style={{ height: "8px" }}>
        <div
          className={`progress-bar bg-${color}`}
          role="progressbar"
          style={{ width: `${value}%` }}
          aria-valuenow={value}
          aria-valuemin="0"
          aria-valuemax="100"
        ></div>
      </div>
    </div>
  );

  return (
    <div className="mt-5">
      <h3 className="mb-4">📝 Analysis Results</h3>

      {/* AI Feedback */}
      <div className="card mb-4 shadow-sm">
        <div className="card-body">
          <h5 className="card-title">🤖 AI Feedback</h5>
          <div className="mt-3">
            <ReactMarkdown>{ai_feedback}</ReactMarkdown>
          </div>
        </div>
      </div>

      {/* Comparison */}
      <div className="card shadow-sm">
        <div className="card-body">
          <h5 className="card-title mb-4">📊 Comparison Metrics</h5>

          {renderProgressBar("Skill Match", comparison.skill_match, "primary")}
          {renderProgressBar(
            "Experience Match",
            comparison.experience_match,
            "success"
          )}
          {renderProgressBar(
            "Project Alignment",
            comparison.project_alignment,
            "info"
          )}

          {comparison.missing_skills &&
            comparison.missing_skills.length > 0 && (
              <>
                <strong>Missing Skills:</strong>
                <div className="mt-2">
                  {comparison.missing_skills.map((skill, index) => (
                    <span key={index} className="badge bg-danger me-2 mb-2">
                      {skill}
                    </span>
                  ))}
                </div>
              </>
            )}
        </div>
      </div>
    </div>
  );
}
