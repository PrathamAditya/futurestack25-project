from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os
import config
import tools   # 👈 NEW - centralizes all MCP tool imports
from resume_parser import parse_resume
from exa_tool import enrich_job_description
from job_matcher import compare_resume_to_jd
from cerebras_client import review_resume
from interview_question_tool import generate_interview_questions_advanced
from interview_tool import evaluate_interview_answers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost:3000"] for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...), job_description: str = Form(...)):
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Extract structured resume data
    resume_data = parse_resume(tmp_path, file.filename)
    os.remove(tmp_path)

    # Enrich JD
    enriched_jd_info = enrich_job_description(job_description)

    # Compare Resume vs JD
    comparison_result = compare_resume_to_jd(resume_data, enriched_jd_info)

    # AI feedback
    ai_feedback = review_resume(resume_data["raw_text"], enriched_jd_info)

    return {
        "resume": resume_data,
        "jd_info": enriched_jd_info,
        "comparison": comparison_result,
        "ai_feedback": ai_feedback
    }

@app.post("/interview/generate-advanced")
async def generate_advanced_questions(request):
    data = await request.json()
    resume_text = data.get("resume_text")
    num_questions = data.get("num_questions", 5)
    return generate_interview_questions_advanced(resume_text, num_questions)

@app.post("/interview/evaluate")
async def evaluate_interview(request):
    data = await request.json()
    resume_text = data.get("resume_text")
    qa_pairs = data.get("qa_pairs", [])
    return evaluate_interview_answers(resume_text, qa_pairs)


