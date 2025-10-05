from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from config import CEREBRAS_API_KEY

client = Cerebras(
  api_key=CEREBRAS_API_KEY
)
def review_resume(resume_text, jd_info=None):
    prompt = f"""
You are an experienced **Technical Hiring Assistant** and **AI Career Coach**.

Analyze the following **Resume** and **Job Description** carefully and provide a **professional, concise, Markdown-formatted** report with the following sections:

## 📄 Resume Analysis
- Highlight the **most important technical skills**, tools, frameworks, and domains.
- Summarize **relevant experience** (years, industries, notable achievements).
- Note **education**, certifications, and any standout strengths.

## 📝 Job Description Analysis
- Extract and summarize **key technical requirements**, soft skills, and experience levels.
- Identify any **must-have qualifications** mentioned explicitly.

## 📊 Comparison Snapshot
Provide a **crisp 4-point summary**:
- **Skill Match:** X % — (brief explanation)
- **Experience Match:** X % — (brief explanation)
- **Missing / Underrepresented Skills:** list 3–5 key gaps
- **Overall Alignment:** 2–3 sentences on how well the resume matches the JD

## 🚀 Recommendations
Provide **specific, actionable suggestions** (3–5 bullet points) to improve the resume or interview readiness:
- Focus on **missing skills**
- **Resume phrasing** improvements if relevant
- **Preparation areas** for likely questions based on gaps

---
**Resume Text:**  
{resume_text}

**Job Description Info:**  
{jd_info}
"""

    messages = [
        {"role": "system", "content": "You are a structured, concise, and professional AI hiring assistant. Always return clean Markdown. Avoid fluff."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        messages=messages,
        model="llama-4-scout-17b-16e-instruct",
        temperature=0.3,
        max_tokens=1200
    )

    return response.choices[0].message.content

