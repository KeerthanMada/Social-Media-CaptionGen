import os
from typing import Optional
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import httpx
from pydantic import BaseModel
import json

app = FastAPI(title="Social Media Caption Generator")

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# API Configuration
WEBUI_ENABLED = True
WEBUI_BASE_URL = "https://chat.ivislabs.in/api"
API_KEY = "sk-fa41b818714e45ed917700badd46ef36"
DEFAULT_MODEL = "gemma2:2b"

class CaptionRequest(BaseModel):
    content_theme: str
    num_captions: int = 3
    brand_voice: Optional[str] = "engaging"

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_captions(
    content_theme: str = Form(...),
    num_captions: int = Form(3),
    brand_voice: str = Form("engaging"),
    model: str = Form(DEFAULT_MODEL)
):
    try:
        prompt = f"Generate {num_captions} engaging social media post captions for the theme '{content_theme}', using a '{brand_voice}' brand voice."
        
        if WEBUI_ENABLED:
            try:
                messages = [{"role": "user", "content": prompt}]
                request_payload = {"model": model, "messages": messages}
                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        f"{WEBUI_BASE_URL}/chat/completions",
                        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
                        json=request_payload,
                        timeout=60.0
                    )
                    if response.status_code == 200:
                        result = response.json()
                        generated_text = result.get("choices", [{}])[0].get("message", {}).get("content", "")
                        return {"generated_captions": generated_text}
            except Exception as e:
                print(f"API error: {str(e)}")

        raise HTTPException(status_code=500, detail="Failed to generate captions")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating captions: {str(e)}")

@app.get("/models")
async def get_models():
    try:
        if WEBUI_ENABLED:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{WEBUI_BASE_URL}/models", headers={"Authorization": f"Bearer {API_KEY}"})
                if response.status_code == 200:
                    models_data = response.json()
                    model_names = [model["id"] for model in models_data.get("data", []) if "id" in model]
                    if model_names:
                        return {"models": model_names}
    except Exception as e:
        print(f"Error fetching models: {str(e)}")
    return {"models": [DEFAULT_MODEL]}
