import re
import json
from cerebras_client import client


# @Tool(name="generate_interview_questions", description="Generate tailored interview questions based on the candidate's resume")
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
        temperature=0.2,
        max_tokens=800
    )

    return response.choices[0].message.content


# @Tool(name="evaluate_interview_answers", description="Evaluate candidate's answers to the generated interview questions")
def evaluate_interview_answers(resume_text: str, qa_pairs: list):
    """
    qa_pairs format:
    [
      { "question": "...", "answer": "..." },
      ...
    ]
    """
    prompt = f"""
You are a **senior technical interviewer at a top Silicon Valley company**. Your task is to fairly and rigorously evaluate a candidate's interview answers based on their resume and the provided question-answer pairs.

📄 Candidate Resume:
{resume_text}

📝 Candidate's Answers (strict JSON):
```json
{qa_json}
For each answer, evaluate carefully and return:
question: exactly as given in the input (do NOT modify wording)
answer: exactly as given by the candidate (do NOT rewrite, infer, or "improve" the answer)
score: a number from 1 to 5, based on the following criteria:
5 = Excellent: precise, technically correct, well-structured, demonstrates deep understanding and clear communication.
4 = Good: mostly correct, minor omissions, shows solid understanding.
3 = Average: partial answer, lacks depth or clarity, some gaps.
2 = Weak: vague or incorrect in key areas, missing structure or logic.
1 = Poor: fundamentally incorrect, irrelevant, or no real attempt (e.g., "I don't know").
feedback: 2–3 sentences of specific, constructive feedback on how the answer could be improved. Be direct but helpful.
After evaluating all answers, calculate:
overall_score: the average score across all answers, rounded to 1 decimal place.
summary_feedback: a 2–3 sentence overall performance summary. Comment on the candidate’s technical ability, clarity, and communication style. Mention strengths and key improvement areas.
Output formatting rules:
Return ONLY a valid JSON object in the following structure:
{
  "results": [
    {
      "question": "...",
      "answer": "...",
      "score": 4,
      "feedback": "..."
    }
  ],
  "overall_score": 4.2,
  "summary_feedback": "..."
}
Do NOT include any text before or after the JSON object.
If the answer is "I don't know" or similar, score it as 1 and give clear feedback explaining why.
Do NOT rewrite or generate new answers under any circumstances.
"""
    llama_response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-4-scout-17b-16e-instruct",
        temperature=0.0,
        max_tokens=1200
    )
    content = llama_response.choices[0].message.content
    print(content)
    json_match = re.search(r"```json\s*(.*?)\s*```", content, re.DOTALL)
    if json_match:
        json_str = json_match.group(1).strip()
    else:
        json_str = content.strip()
    try:
        response = json.loads(json_str)
        return response
    except json.JSONDecodeError:
        return []
