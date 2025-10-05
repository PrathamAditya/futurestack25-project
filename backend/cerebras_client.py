from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from config import CEREBRAS_API_KEY

client = Cerebras(
  api_key=CEREBRAS_API_KEY
)
def review_resume(resume_text, jd_info=None):
    prompt = f"""
You are an experienced **Technical Hiring Assistant** and **AI Career Coach**.

Analyze the candidate's **Resume** in the context of the provided **Job Description**, and provide a **professional, opinionated, Markdown-formatted** response with ONLY the following section:

## 📄 Resume Analysis
Write **4–5 concise bullet points** that reflect **your evaluation of the resume**, not just extracted information. 
Focus on:
- How well the candidate’s **skills and experience align** with the job description.
- The **strength and clarity** of their technical profile.
- **Notable strengths or differentiators** that stand out to a hiring manager.
- Any **gaps or weaknesses** that may affect their fit (in a neutral, professional tone).

Do NOT just list keywords or restate the resume.
Do NOT include recommendations, introductions, or explanations outside the bullet points.

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
        temperature=0.1,
        max_tokens=1200
    )

    return response.choices[0].message.content

