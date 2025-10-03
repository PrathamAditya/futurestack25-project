import React from "react";

export default function JobDescriptionInput({
  jobDescription,
  setJobDescription,
}) {
  return (
    <div className="mb-3">
      <label className="form-label">Job Description</label>
      <textarea
        className="form-control"
        rows="5"
        placeholder="Paste the job description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        required
      ></textarea>
    </div>
  );
}
