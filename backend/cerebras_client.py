from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv
from config import CEREBRAS_API_KEY

client = Cerebras(
  api_key=CEREBRAS_API_KEY
)
def review_resume(resume_text, jd_info=None):
    prompt = f"""
You are an experienced **Technical Hiring Assistant** and **AI Career Coach**.

Analyze the following **Resume** in the context of the **Job Description**, and provide a **concise, professional Markdown-formatted** response with ONLY the following section:

## 📄 Resume Analysis
Summarize the candidate's profile in **4–5 short bullet points**, focusing on:
- Key **technical skills** and tools mentioned
- Relevant **experience and achievements**
- **Certifications** or education that stand out
- Any **notable strengths** or highlights relevant to the job

Do NOT include recommendations, introductions, explanations, or any other sections.  
Keep it crisp, factual, and structured.

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

