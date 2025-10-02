import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a resume first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload-resume", {
      method: "POST",
      body: formData,
    });

    const result = await response.json();
    console.log(result);
    alert(JSON.stringify(result, null, 2));
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Resume Analyzer</h2>
      <input
        type="file"
        className="form-control mb-3"
        accept=".pdf,.doc,.docx"
        onChange={handleFileChange}
      />
      <button className="btn btn-primary" onClick={handleUpload}>
        Upload & Analyze
      </button>
    </div>
  );
}

export default App;
