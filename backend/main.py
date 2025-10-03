from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import tempfile
import os

from resume_parser import parse_resume
from exa_tool import enrich_job_description
from job_matcher import compare_resume_to_jd
from cerebras_client import review_resume


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:3000"], 
    allow_origins=["*"], # or ["*"] to allow all origins
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

    # AI feedback (placeholder for now)
    ai_feedback = review_resume(resume_data["raw_text"], enriched_jd_info)

    return {
        "resume": resume_data,
        "jd_info": enriched_jd_info,
        "comparison": comparison_result,
        "ai_feedback": ai_feedback
    }
