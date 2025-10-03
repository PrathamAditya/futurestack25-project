from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from config import CEREBRAS_API_KEY

client = Cerebras(
  api_key=CEREBRAS_API_KEY
)

def review_resume(resume_text, jd_info=None):
    prompt = f"""
You are an AI career coach and technical hiring assistant.

Analyze the following **resume** and **job description information**, then return your answer in **Markdown format** with these sections:

## Resume Analysis
(Highlight key technical skills, experience, education, certifications, and unique strengths.)

## Job Description Analysis
(Highlight the required skills, experience, and soft skills.)

## Comparison
- Skill match %
- Experience match %
- Missing or underrepresented skills
- Alignment insights

## Recommendations
(Provide clear, actionable suggestions to improve the resume or prepare for interviews based on gaps.)

---
Resume:
{resume_text}

Job Description Info:
{jd_info}
"""
    messages = [
        {"role": "system", "content": "You are a structured, concise, and professional AI resume reviewer."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="llama-4-scout-17b-16e-instruct"
    )

    return response.choices[0].message.content

