import React, { useState } from "react";
import "./UploadForm.css";
import { API_BASE_URL } from "../config";

export default function UploadForm({ onAnalysisComplete }) {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setFile(e.target.files[0]);
  const handleJDChange = (e) => setJobDescription(e.target.value);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file || !jobDescription) {
      alert("Please upload a resume and enter a job description");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    try {
      const res = await fetch(`${API_BASE_URL}/upload-resume`, {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      onAnalysisComplete(data);
    } catch (err) {
      console.error(err);
      alert("Error uploading resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="step-card upload-form fade-in">
      <h3 className="mb-4">Upload Resume & Write Job Description</h3>

      <form onSubmit={handleSubmit}>
        {/* Resume Upload */}
        <div className="mb-3">
          <label className="form-label">Resume (PDF / DOCX)</label>
          <input
            type="file"
            accept=".pdf,.doc,.docx"
            className="form-control"
            onChange={handleFileChange}
          />
        </div>

        {/* Job Description */}
        <div className="mb-3">
          <label className="form-label">📝 Job Description</label>
          <textarea
            rows="4"
            value={jobDescription}
            onChange={handleJDChange}
            className="form-control job-description-textarea"
            placeholder="Paste the job description here..."
          />
        </div>

        <button
          className="btn btn-primary w-100"
          type="submit"
          disabled={loading}
        >
          {loading ? (
            <>
              <span className="spinner-border spinner-border-sm me-2"></span>
              Analyzing...
            </>
          ) : (
            "Upload & Analyze"
          )}
        </button>
      </form>
    </div>
  );
}
