import React, { useState } from "react";

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
      const res = await fetch("http://127.0.0.1:8000/upload-resume", {
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
    <div className="card">
      <h2>Upload Resume</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <label>Resume (PDF / DOCX)</label>
          <input
            type="file"
            accept=".pdf,.doc,.docx"
            onChange={handleFileChange}
          />
        </div>

        <div className="mb-3">
          <label>Job Description</label>
          <textarea rows="4" value={jobDescription} onChange={handleJDChange} />
        </div>

        <button className="btn btn-primary" type="submit" disabled={loading}>
          {loading ? "Analyzing..." : "Upload & Analyze"}
        </button>
      </form>
    </div>
  );
}
