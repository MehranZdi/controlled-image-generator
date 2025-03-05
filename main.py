from fastapi import FastAPI
from diffusers import StableDiffusionPipeline
import torch
import os

app = FastAPI()

print("Loading the diffusion model...")
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
print("Model loaded successfully!")

os.makedirs('static', exist_ok=True)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Controlled Image Generator API is running!"}