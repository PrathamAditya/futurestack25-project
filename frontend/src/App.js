import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import UploadForm from "./components/UploadForm";
import Results from "./components/Results";
import QuestionList from "./components/QuestionList";
import EvaluationResults from "./components/EvaluationResults";

function App() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [qaPairs, setQaPairs] = useState(null);
  const [evaluationResults, setEvaluationResults] = useState(null);

  // 🧠 When qaPairs changes, trigger evaluation call
  useEffect(() => {
    const evaluateAnswers = async () => {
      if (!qaPairs || !analysisResult) return;

      try {
        const response = await fetch(
          "http://127.0.0.1:8000/interview/evaluate",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              resume_text: analysisResult?.resume?.raw_text,
              qa_pairs: qaPairs,
            }),
          }
        );

        const data = await response.json();
        setEvaluationResults(data);
      } catch (err) {
        console.error(err);
        alert("Failed to evaluate answers");
      }
    };

    evaluateAnswers();
  }, [qaPairs, analysisResult]);

  return (
    <div>
      <div className="navbar">⚡ AI Interview Assistant</div>
      <div className="container">
        <UploadForm onAnalysisComplete={setAnalysisResult} />
        <Results result={analysisResult} />
        {analysisResult && (
          <QuestionList
            resumeText={analysisResult?.resume?.raw_text}
            onSubmitAnswers={setQaPairs}
          />
        )}
        {evaluationResults && <EvaluationResults results={evaluationResults} />}
      </div>
    </div>
  );
}

export default App;
