import React from "react";

export default function JobDescriptionInput({ value, onChange }) {
  return (
    <div className="mb-3">
      <label>Job Description</label>
      <textarea
        rows="4"
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
    </div>
  );
}
