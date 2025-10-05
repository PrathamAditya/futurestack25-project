import os
from exa_py import Exa
from dotenv import load_dotenv
from config import EXA_API_KEY
import re
import logging

logger = logging.getLogger(__name__)
exa_client = Exa(api_key=EXA_API_KEY)

def enrich_job_description(job_description: str, num_results=20):
    """
    Enrich a job description using Exa's neural search to extract trending skills and technologies.
    Returns structured info for matching: skills_required and experience_required.
    """
    if not EXA_API_KEY:
        logger.warning("⚠️ EXA_API_KEY not found — skipping enrichment and returning minimal structure.")
        return {
            "skills_required": [],
            "experience_required": None
        }

    logger.info(f"Enriching JD via Exa for: {job_description}")

    try:
        results = exa_client.search_and_contents(
            f"Top frameworks, libraries, technologies, and skills for the role: {job_description}",
            type="auto",
            num_results=num_results,
            text={"max_characters": 800}
        ).results

        snippets = [r.text for r in results if r.text and len(r.text) > 80]
        if not snippets:
            logger.warning("No relevant snippets found from Exa.")
            return {
                "skills_required": [],
                "experience_required": None
            }

        combined_text = " ".join(snippets)
        skill_pattern = re.compile(r"\b[A-Z][a-zA-Z0-9\+\#\.\-]{2,}\b")
        raw_skills = skill_pattern.findall(combined_text)

        # Normalize and filter duplicates
        clean_skills = list({skill.strip(",.()") for skill in raw_skills})

        # Heuristic: prioritize top 20 unique skills
        top_skills = clean_skills[:20]

        logger.info(f"Extracted skills: {top_skills}")
        exp_match = re.search(r"(\d+)\s*\+?\s*years?", combined_text, re.IGNORECASE)
        experience_required = int(exp_match.group(1)) if exp_match else None

        return {
            "skills_required": top_skills,
            "experience_required": experience_required
        }

    except Exception as e:
        logger.error(f"Error during Exa enrichment: {e}")
        return {
            "skills_required": [],
            "experience_required": None
        }