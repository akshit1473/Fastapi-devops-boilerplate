import os
from fastapi import FastAPI
from app.schemas import QueryRequest
from app.security import sanitize_input_prompt

app = FastAPI(title="My AI Backend Engine", version="1.0.0")

@app.get("/", status_code=200)
@app.get("/health", status_code=200)
async def health_check():
    return {
        "status": "healthy",
        "environment": os.getenv("ENVIRONMENT", "development"),
        "security": "hardened-non-root",
        "user_id": os.getuid() if hasattr(os, "getuid") else "N/A"
    }

@app.post("/api/v1/query")
async def process_ai_query(payload: QueryRequest):
    # 1. Pydantic validates payload structure (QueryRequest)
    # 2. Sanitize against prompt injections
    clean_prompt = sanitize_input_prompt(payload.prompt)
    
    return {
        "status": "processed",
        "clean_prompt": clean_prompt,
        "user_id": payload.user_id
    }
