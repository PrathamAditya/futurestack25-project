def enrich_job_description(job_description):
    # Simple keyword extraction mock
    if "developer" in job_description.lower():
        return {
            "skills_required": ["Python", "React", "Docker", "AWS"],
            "experience_required": 2
        }
    elif "data" in job_description.lower():
        return {
            "skills_required": ["Python", "SQL", "Pandas", "Azure"],
            "experience_required": 3
        }
    else:
        return {
            "skills_required": ["Communication", "Problem Solving"],
            "experience_required": 1
        }