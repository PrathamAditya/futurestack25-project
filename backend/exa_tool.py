import os
from exa_py import Exa
from dotenv import load_dotenv
from config import EXA_API_KEY

exa_client = Exa(api_key=EXA_API_KEY)

def enrich_job_description(job_description: str, num_results=5):
    """
    Enrich a job description using Exa's neural search to extract trending skills and technologies.
    """
    if not EXA_API_KEY:
        print("⚠️ EXA_API_KEY not set. Returning fallback.")
        return {
            "skills_required": ["Communication", "Problem Solving"],
            "experience_required": 1
        }

    print(f"🔍 Enriching JD via Exa for: {job_description}")

    # Search web with Exa
    try:
        results = exa_client.search_and_contents(
            f"Top frameworks, libraries, and skills required for this job: {job_description}",
            type="auto",
            num_results=num_results,
            text={"max_characters": 800}
        ).results

        snippets = []
        for r in results:
            if r.text and len(r.text) > 100:
                snippets.append(r.text)

        combined_text = " ".join(snippets)
        if not combined_text:
            print("⚠️ No Exa results, using fallback.")
            return {
                "skills_required": ["Communication", "Problem Solving"],
                "experience_required": 1
            }

        # Very basic skill extraction: capitalized keywords
        extracted_skills = set()
        for word in combined_text.split():
            word = word.strip(",.()")
            if word.isalpha() and word[0].isupper() and len(word) > 2:
                extracted_skills.add(word)

        skills_list = list(extracted_skills)[:20]

        print(f"✅ Extracted skills from Exa: {skills_list}")

        return {
            "skills_required": skills_list if skills_list else ["Communication", "Problem Solving"],
            "experience_required": 1
        }

    except Exception as e:
        print(f"❌ Exa enrichment error: {e}")
        return {
            "skills_required": ["Communication", "Problem Solving"],
            "experience_required": 1
        }
