import React, { useState } from "react";

export default function QuestionList({ resumeText, onSubmitAnswers }) {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(false);

  const fetchQuestions = async () => {
    if (!resumeText) {
      alert("Please analyze resume first.");
      return;
    }
    setLoading(true);
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/interview/generate-advanced",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ resume_text: resumeText, num_questions: 5 }),
        }
      );

      const data = await response.json();

      // If backend returns string JSON, parse it
      const parsed = typeof data === "string" ? JSON.parse(data) : data;
      setQuestions(parsed);
    } catch (err) {
      console.error(err);
      alert("Failed to fetch questions");
    } finally {
      setLoading(false);
    }
  };

  const handleAnswerChange = (index, value) => {
    setAnswers({ ...answers, [index]: value });
  };

  const handleSubmit = () => {
    const qaPairs = questions.map((q, i) => ({
      question: q.question || q,
      answer: answers[i] || "",
    }));

    onSubmitAnswers(qaPairs);
  };

  return (
    <div className="card mt-4">
      <h2>Answer Questions</h2>

      {!questions.length ? (
        <button
          className="btn btn-primary"
          onClick={fetchQuestions}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Interview Questions"}
        </button>
      ) : (
        <div>
          {questions.map((q, i) => (
            <div key={i} className="mb-3">
              <label>
                <strong>Q{i + 1}:</strong> {q.question || q}
              </label>
              <textarea
                rows="3"
                className="form-control mt-2"
                value={answers[i] || ""}
                onChange={(e) => handleAnswerChange(i, e.target.value)}
              />
            </div>
          ))}

          <button className="btn btn-primary" onClick={handleSubmit}>
            Submit Answers for Evaluation
          </button>
        </div>
      )}
    </div>
  );
}
