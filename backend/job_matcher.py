def compare_resume_to_jd(resume_text, jd_info):
    """
    Simple metric-based scoring:
    - Skill match %
    - Experience relevance (can be mocked for MVP)
    - Project alignment %
    """
    # For now, mock scores for MVP
    return {
        "skill_match": "75%",
        "experience_match": "80%",
        "project_alignment": "70%"
    }
