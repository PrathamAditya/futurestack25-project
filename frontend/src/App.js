import React, { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import UploadForm from "./components/UploadForm";
import Results from "./components/Results";
import QuestionList from "./components/QuestionList";
import EvaluationResults from "./components/EvaluationResults";
import { API_BASE_URL } from "./config";

function App() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [qaPairs, setQaPairs] = useState(null);
  const [evaluationResults, setEvaluationResults] = useState(null);

  useEffect(() => {
    const evaluateAnswers = async () => {
      if (!qaPairs || !analysisResult) return;
      try {
        const response = await fetch(`${API_BASE_URL}/interview/evaluate`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            resume_text: analysisResult?.resume?.raw_text,
            qa_pairs: qaPairs,
          }),
        });
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
    <div className="app-bg min-vh-100">
      <nav className="navbar justify-content-center">
        <div className="container d-flex justify-content-center">
          <h1 className="app-title mb-0 text-center">
            AI Resume & Interview Evaluator
          </h1>
        </div>
      </nav>
      <div className="container py-5">
        {/* STEP 1 */}
        <div className="step-card fade-in">
          <UploadForm onAnalysisComplete={setAnalysisResult} />
        </div>

        {/* STEP 2 */}
        {analysisResult && (
          <div className="step-card fade-in">
            <Results result={analysisResult} />
          </div>
        )}

        {/* STEP 3 */}
        {analysisResult && (
          <div className="step-card fade-in">
            <QuestionList
              resumeText={analysisResult?.resume?.raw_text}
              onSubmitAnswers={setQaPairs}
            />
          </div>
        )}

        {/* STEP 4 */}
        {evaluationResults && (
          <div className="step-card fade-in">
            <EvaluationResults results={evaluationResults} />
          </div>
        )}

        {/* Footer 
        <footer className="footer text-center py-3">
          <div className="container">
            <p className="mb-0">
              Built for <strong>FutureStack25 Hackathon</strong> ·
              <a
                href="https://github.com/PrathamAditya/futurestack25-project"
                target="_blank"
                rel="noopener noreferrer"
                className="footer-link ms-1"
              >
                View on GitHub
              </a>
            </p>
          </div>
        </footer> */}
      </div>
    </div>
  );
}

export default App;
