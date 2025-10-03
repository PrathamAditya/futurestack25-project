def compare_resume_to_jd(resume_data, jd_info):
    """
    Compare parsed resume JSON with job description info (skills, exp, projects).
    Returns scoring metrics.
    """

    resume_skills = set([s.lower() for s in resume_data.get("skills", [])])
    jd_skills = set([s.lower() for s in jd_info.get("skills_required", [])])

    # Skill Match %
    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills - resume_skills
    skill_match = int((len(matched_skills) / len(jd_skills)) * 100) if jd_skills else 0

    # Experience Match % (basic: years of exp vs JD requirement)
    resume_exp = resume_data.get("experience_years", 0)
    jd_exp = jd_info.get("experience_required", 0)
    exp_match = min(100, int((resume_exp / jd_exp) * 100)) if jd_exp > 0 else 70

    # Project Alignment (mock: if JD keywords appear in project text)
    projects = " ".join(resume_data.get("projects", []))
    project_hits = sum(1 for skill in jd_skills if skill in projects.lower())
    project_alignment = int((project_hits / len(jd_skills)) * 100) if jd_skills else 0

    return {
        "skill_match": skill_match,
        "experience_match": exp_match,
        "project_alignment": project_alignment,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
