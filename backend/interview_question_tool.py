import re
from config import EXA_API_KEY, CEREBRAS_API_KEY
from exa_py import Exa
from cerebras.cloud.sdk import Cerebras
from mcp.server.fastapi import Tool

exa_client = Exa(api_key=EXA_API_KEY)
llm_client = Cerebras(api_key=CEREBRAS_API_KEY)

def extract_top_skills_from_resume(resume_text: str, top_n=2):
    """
    Very simple skill extractor using capitalized keywords.
    You could later make this smarter (e.g. regex, embedding, etc.)
    """
    words = re.findall(r"\b[A-Z][a-zA-Z0-9\+\#]{2,}\b", resume_text)
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    sorted_skills = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [s for s, _ in sorted_skills[:top_n]]


def search_exa_for_questions(skill: str, num_results=3):
    """
    Use Exa to search web for top interview questions related to a specific skill.
    """
    query = f"Top {skill} interview questions for experienced developers"
    print(f"🔍 Exa searching for questions about: {skill}")

    results = exa_client.search_and_contents(
        query,
        type="auto",
        num_results=num_results,
        text={"max_characters": 1000}
    ).results

    snippets = []
    for r in results:
        if r.text and len(r.text) > 50:
            snippets.append(r.text)
    return snippets


def refine_questions_with_llama(resume_text: str, raw_snippets: list, num_questions=5):
    """
    Use LLaMA to pick the best questions and rewrite them.
    """
    prompt = f"""
You are an AI interviewer.

Candidate Resume:
{resume_text}

Here are raw interview questions and snippets from the web:
{raw_snippets}

Pick the {num_questions} most relevant and high-quality questions based on the candidate's skills.
Rewrite them cleanly and clearly. Include at least one scenario-based and one soft skill question.

Return a JSON array like:
[
  {{ "question": "..." }},
  ...
]
"""
    response = llm_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-4-scout-17b-16e-instruct",
        temperature=0.4,
        max_tokens=1000
    )

    return response.choices[0].message.content


@Tool(name="generate_interview_questions_advanced", description="Generates high-quality interview questions by combining Exa search with LLaMA refinement.")
def generate_interview_questions_advanced(resume_text: str, num_questions: int = 5):
    """
    Full pipeline:
    1. Extract top skills
    2. Search Exa for raw questions
    3. Refine with LLaMA
    """
    skills = extract_top_skills_from_resume(resume_text)
    if not skills:
        return {"error": "No skills found in resume"}

    print(f"🧠 Top extracted skills: {skills}")

    all_snippets = []
    for skill in skills:
        snippets = search_exa_for_questions(skill)
        all_snippets.extend(snippets)

    if not all_snippets:
        return {"error": "No raw questions found from Exa"}

    refined = refine_questions_with_llama(resume_text, all_snippets, num_questions)
    return refined
