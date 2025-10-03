import React, { useState } from "react";
import JobDescriptionInput from "./JobDescriptionInput";
import { analyzeResume } from "../api";

export default function UploadForm({ setResult }) {
  const [file, setFile] = useState(null);
  const [jobDescription, setJobDescription] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file || !jobDescription) {
      alert("Please upload a resume and provide a job description.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    const data = await analyzeResume(formData);
    setResult(data);
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4">
      <div className="mb-3">
        <label className="form-label">Upload Resume</label>
        <input
          type="file"
          className="form-control"
          accept=".pdf,.doc,.docx"
          onChange={handleFileChange}
          required
        />
      </div>

      <JobDescriptionInput
        jobDescription={jobDescription}
        setJobDescription={setJobDescription}
      />

      <button type="submit" className="btn btn-primary">
        Analyze Resume
      </button>
    </form>
  );
}
