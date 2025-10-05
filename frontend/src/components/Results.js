import React from "react";
import ReactMarkdown from "react-markdown";

export default function Results({ result }) {
  if (!result) return null;

  const { resume, jd_info, comparison, ai_feedback } = result;

  return (
    <div className="fade-in">
      <h3>Resume Analysis</h3>

      <div className="mb-3">
        <h5>Skills Extracted</h5>
        <p>{resume.skills?.join(", ") || "No skills detected"}</p>
      </div>

      <div className="mb-3">
        <h5>..Job Description Summary</h5>
        <p>{jd_info?.summary || "No summary available"}</p>
      </div>

      <div className="mb-3">
        <h5>AI Feedback</h5>
        <div className="feedback-box">
          <ReactMarkdown>
            {ai_feedback || "No feedback available"}
          </ReactMarkdown>
        </div>
      </div>

      <div className="mb-3">
        <h5>Matching Scores</h5>
        {comparison && (
          <ul>
            <li>Skill Match: {comparison.skill_match}</li>
            <li>Experience Match: {comparison.experience_match}</li>
            <li>Project Alignment: {comparison.project_alignment}</li>
          </ul>
        )}
      </div>
    </div>
  );
}
