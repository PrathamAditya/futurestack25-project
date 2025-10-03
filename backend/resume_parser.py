import fitz  # PyMuPDF
import docx
import re

def extract_text_from_pdf(file_path):
    text = ""
    pdf = fitz.open(file_path)
    for page in pdf:
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])

def parse_resume(file_path, original_filename):
    """
    Extracts text and returns structured resume data
    """
    if original_filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif original_filename.lower().endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

    # Extract skills (basic keyword match for MVP)
    skills = re.findall(r"\b(Python|Java|React|Node|Docker|AWS|Azure|C\+\+|SQL|Kubernetes)\b", text, re.IGNORECASE)

    # Extract education
    education = []
    if "B.Tech" in text or "Bachelor" in text:
        education.append("Bachelor’s Degree")
    if "M.Tech" in text or "Master" in text:
        education.append("Master’s Degree")

    # Extract simple experience keywords
    experience_years = 0
    exp_match = re.search(r"(\d+)\+?\s+years", text, re.IGNORECASE)
    if exp_match:
        experience_years = int(exp_match.group(1))

    # Projects (mock: split on "Project" word)
    projects = [p.strip() for p in text.split("Project") if len(p) > 30]

    return {
        "raw_text": text,
        "skills": list(set([s.capitalize() for s in skills])),
        "education": education,
        "experience_years": experience_years,
        "projects": projects[:3] 
    }
