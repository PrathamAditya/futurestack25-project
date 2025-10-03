# backend/interview_tool.py
from mcp.server.fastapi import Tool
from cerebras_client import client

@Tool(name="generate_interview_questions", description="Generate tailored interview questions based on the candidate's resume")
def generate_interview_questions(resume_text: str, num_questions: int = 5):
    prompt = f"""
You are a skilled technical interviewer. Given the following resume:

{resume_text}

Generate {num_questions} interview questions that assess the candidate's real understanding.
Focus on their strongest skills and include scenario-based and soft-skill questions.

Return a JSON array like:
[
  {{ "question": "..." }},
  ...
]
"""
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-4-scout-17b-16e-instruct",
        temperature=0.4,
        max_tokens=800
    )

    return response.choices[0].message.content


@Tool(name="evaluate_interview_answers", description="Evaluate candidate's answers to the generated interview questions")
def evaluate_interview_answers(resume_text: str, qa_pairs: list):
    """
    qa_pairs format:
    [
      { "question": "...", "answer": "..." },
      ...
    ]
    """
    prompt = f"""
You are a strict but fair interviewer. A candidate with the following resume:

{resume_text}

Gave the following answers to their interview questions:

{qa_pairs}

For each answer:
- Give a score from 1 to 5.
- Provide constructive feedback.

Return JSON:
[
  {{
    "question": "...",
    "answer": "...",
    "score": 4,
    "feedback": "..."
  }},
  ...
]

Also include:
"overall_score": average of all answers
"summary_feedback": 2-3 sentences overall performance.
"""
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-4-scout-17b-16e-instruct",
        temperature=0.3,
        max_tokens=1200
    )

    return response.choices[0].message.content
