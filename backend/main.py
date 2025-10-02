from fastapi import FastAPI, UploadFile, Form, File
from fastapi.middleware.cors import CORSMiddleware
from resume_parser import extract_text_from_pdf
from exa_tool import enrich_job_description
from job_matcher import compare_resume_to_jd
from cerebras_client import review_resume

app = FastAPI()
# Allow React frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-resume")
async def upload_resume(resume: UploadFile, job_description: str = Form(...)):
    # Step 1: Save uploaded file temporarily
    temp_file = f"temp_{resume.filename}"
    with open(temp_file, "wb") as f:
        f.write(await resume.read())

    # Step 2: Parse resume
    resume_text = extract_text_from_pdf(temp_file)

    # Step 3: Enrich JD using Exa
    enriched_jd_info = enrich_job_description(job_description)

    # Step 4: Compare resume to JD (fit scoring)
    comparison_result = compare_resume_to_jd(resume_text, enriched_jd_info)

    # Step 5: Send everything to LLaMA via Cerebras
    ai_feedback = review_resume(resume_text, enriched_jd_info)

    # Step 6: Aggregate results
    response = {
        "comparison": comparison_result,
        "ai_feedback": ai_feedback
    }

    return response
