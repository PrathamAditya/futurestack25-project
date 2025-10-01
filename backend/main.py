import os
from fastapi import FastAPI
from pydantic import BaseModel
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Cerebras client
client = Cerebras(api_key=os.getenv("CEREBRAS_API_KEY"))

# FastAPI app
app = FastAPI(title="FutureStack25 Project")

# Request body schema
class UserRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"message": "Welcome to FutureStack25 project 🚀"}

@app.post("/chat")
def chat(req: UserRequest):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": req.prompt}],
            model="llama-4-scout-17b-16e-instruct",
        )
        return {"response": chat_completion.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
