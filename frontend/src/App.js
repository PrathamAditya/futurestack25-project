import React, { useState } from "react";
import UploadForm from "./components/UploadForm";
import Results from "./components/Results";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="container mt-5">
      <h2 className="mb-4">🚀 Resume Analyzer</h2>
      <UploadForm setResult={setResult} />
      <Results result={result} />
    </div>
  );
}

export default App;
