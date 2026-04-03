from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.extractor import extract_insights

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "data/transcripts"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Meeting Intelligence Hub API running"}

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    text = content.decode("utf-8")

    basic = extract_insights(text)

    return {
        "basic_analysis": basic,
        "ai_analysis": "AI disabled for now"
    }