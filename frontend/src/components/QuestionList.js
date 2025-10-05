import React, { useState } from "react";
import { API_BASE_URL } from "../config";

export default function QuestionList({ resumeText, onSubmitAnswers }) {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchQuestions = async () => {
    setLoading(true);
    try {
      const response = await fetch(
        `${API_BASE_URL}/interview/generate-advanced`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            resume_text: resumeText,
            num_questions: 5,
          }),
        }
      );
      const data = await response.json();
      setQuestions(data);
      setAnswers(Array(data.length).fill(""));
    } catch (err) {
      console.error(err);
      alert("Failed to fetch questions");
    } finally {
      setLoading(false);
    }
  };

  const handleAnswerChange = (index, value) => {
    const newAnswers = [...answers];
    newAnswers[index] = value;
    setAnswers(newAnswers);
  };

  const handleSubmit = () => {
    const qaPairs = questions.map((q, i) => ({
      question: q.question || q,
      answer: answers[i] || "",
    }));
    onSubmitAnswers(qaPairs);
  };

  return (
    <div className="fade-in">
      <h3>Answer Interview Questions</h3>

      {/* Generate Button */}
      {questions.length === 0 && (
        <button
          className="btn btn-primary w-100 mb-4"
          onClick={fetchQuestions}
          disabled={loading}
        >
          {loading ? (
            <span>
              <span className="spinner-border spinner-border-sm me-2"></span>
              Generating Questions...
            </span>
          ) : (
            "Generate Questions"
          )}
        </button>
      )}

      {/* Question List */}
      {questions.map((q, idx) => (
        <div key={idx} className="question-card fade-in">
          <h5>Q{idx + 1}:</h5>
          <p>{q.question || q}</p>
          <textarea
            rows="3"
            className="form-control mt-2"
            placeholder="Type your answer here..."
            value={answers[idx] || ""}
            onChange={(e) => handleAnswerChange(idx, e.target.value)}
          ></textarea>
        </div>
      ))}

      {/* Submit Button */}
      {questions.length > 0 && (
        <button
          className="btn btn-primary w-100 mt-3"
          onClick={handleSubmit}
          disabled={answers.some((a) => a.trim() === "")}
        >
          Submit Answers for Evaluation
        </button>
      )}
    </div>
  );
}
