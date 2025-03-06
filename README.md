# Controlled Image Generator API

This is a FastAPI-based image generation API powered by Stable Diffusion. It supports text-to-image generation, sketch-to-image transformation, and style transfer.

## Features

- **Text-to-Image**: Generate images from textual prompts.
- **Sketch-to-Image**: Convert a sketch to a detailed image.
- **Style Transfer**: Apply different artistic styles to generated images.

## Docker Image

A prebuilt Docker image is available on DockerHub:

```
docker pull mehranzdi/controlled-image-api:latest
```

## Installation

To run the API locally:

### Prerequisites

- Python 3.12+
- pip
- GPU with CUDA support (recommended, in case of saving your time)

### Steps

```bash
git clone https://github.com/mehranzdi/controlled-image-api.git
cd controlled-image-api
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://127.0.0.1:8000`.

## Running with Docker

To run the API using Docker:

```bash
docker run -p 8000:8000 mehranzdi/controlled-image-api:latest
```

## API Endpoints

### Health Check

```bash
GET /
```

Response:

```json
{
  "status": "ok",
  "message": "Controlled Image Generator API is running!"
}
```

### Text-to-Image Generation

```bash
POST /text-to-image
```

**Request Body:**

```json
{
  "prompt": "A futuristic city skyline at sunset"
}
```

**Response:**

```json
{
  "message": "Image has been generated successfully.",
  "image_path": "static/generated_image_20250306_120000.png",
  "prompt": "A futuristic city skyline at sunset"
}
```

### Sketch-to-Image Transformation

```bash
POST /sketch-to-image
```

**Request:** Multipart form data with an image file (`sketch`) and an optional `prompt`.

### Style Transfer

```bash
POST /style-transfer
```

**Request Body:**

```json
{
  "prompt": "A mountain landscape",
  "style": "Van Gogh"
}
```

## Contributing

Feel free to fork this repository and submit pull requests!

## License

This project is licensed under the MIT License.

