from fastapi import FastAPI
from fastapi import HTTPException
from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime

app = FastAPI()

print("Loading the diffusion model...")
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-base")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
print("Model loaded successfully!")

os.makedirs('static', exist_ok=True)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Controlled Image Generator API is running!"}


# Text-to-Image endpoint

@app.post("/text-to-image")
async def text_to_image(prompt: str):
    try:
        image = pipe(prompt).images[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = f"static/generated_image_{timestamp}.png"
        image.save(image_path)

        return {
            "message": "Image was generated successfully.",
            "image_path": image_path,
            "prompt": prompt
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    