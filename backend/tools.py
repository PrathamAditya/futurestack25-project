# backend/tools.py
"""
This file centralizes the registration of all MCP tools.
Any function decorated with @Tool and imported here
will be exposed automatically via MCP Gateway.
"""

# ✅ Import all tool modules here so their @Tool decorators are registered
from resume_parser import parse_resume  # If you plan to expose it later
from exa_tool import enrich_job_description
from job_matcher import compare_resume_to_jd
from cerebras_client import review_resume
from interview_tool import generate_interview_questions, evaluate_interview_answers
from interview_question_tool import generate_interview_questions_advanced

# NOTE:
