# Controlled Image Generator API

This is a FastAPI-based image generation API powered by Stable Diffusion. It supports text-to-image generation, sketch-to-image transformation, and style transfer.

## Features

- **Text-to-Image**: Generate images from textual prompts.
- **Sketch-to-Image**: Convert a sketch to a detailed image.
- **Style Transfer**: Apply different artistic styles to generated images.

## Docker Image

A prebuilt Docker image is available on Docker Hub:

```
docker pull mehranzdi/controlled-image-api:latest
```

## Installation

To run the API locally:

### Prerequisites

- Python 3.12+
- pip
- GPU with CUDA support (Recommended, in case of time-saving)

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
  "prompt": "A cute puppy riding a Harley-Davidson"
}
```

**Response:**

```json
{
  "message": "Image has been generated successfully.",
  "image_path": "static/generated_image_20250306_120000.png",
  "prompt": "A cute puppy riding a Harley-Davidson"
}
```

#### Example:

##### Prompt:

> "A cute puppy riding a Harley-Davidson"
  
##### Result:

![Text to Image](https://github.com/MehranZdi/controlled-image-generator/blob/main/examples/generated_image_20250306_151750.png)

### Sketch-to-Image Transformation

```bash
POST /sketch-to-image
```

**Request:** Multipart form data with an image file (`sketch`) and a `prompt`.

#### Example:

##### Prompt:

> "Donald Duck swimming in a river"
  
##### sketch:

![Sketch](https://github.com/MehranZdi/controlled-image-generator/blob/main/examples/sketch.jpg)

##### Result:

![Sketch to Image](https://github.com/MehranZdi/controlled-image-generator/blob/main/examples/generated_image_20250306_153056.png)



### Style Transfer

```bash
POST /style-transfer
```

**Request Body:**

```json
{
  "prompt": "Kobe Bryant in Lakers",
  "style": "Van gogh starry night"
}
```

#### Example:

##### Input Prompt:

> "Kobe Bryant in Lakers"

##### Style:

> "Van Gogh starry night"

##### Result:
![Style Transfer](https://github.com/MehranZdi/controlled-image-generator/blob/main/examples/styled_image_20250306_153623.png)



## Contributing

Feel free to fork this repository and submit pull requests!

## License

This project is licensed under the MIT License.

