from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import UploadFile, File
from diffusers import StableDiffusionPipeline
from datetime import datetime
from PIL import Image
import torch
import os
import io


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
            "message": "Image has been generated successfully.",
            "image_path": image_path,
            "prompt": prompt
            }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/sketch-to-image")
async def sketch_to_image(sketch: UploadFile=File(...), prompt: str=""):
    try:
        image_data = await sketch.read()
        sketch_image = Image.open(io.BytesIO(image_data)).convert("RGB")
        generated_image = pipe(prompt, image=sketch_image).images[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = f"static/generated_image_{timestamp}.png"
        generated_image.save(image_path)
        return {"message": "Image has been generated!"}
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
