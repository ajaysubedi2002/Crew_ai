import os
import uuid
import re
from typing import Type
from pydantic import BaseModel, Field, PrivateAttr
from crewai.tools import BaseTool
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

class ImageToolInput(BaseModel):
    """Input schema for the image generator."""
    prompt: str = Field(..., description="A simple descriptive prompt for image generation. Avoid special characters.")


class BlogImageGeneratorTool(BaseTool):
    name: str = "blog_image_generator"
    description: str = "Generates blog images. Pass a simple prompt without quotes or special characters."
    args_schema: Type[BaseModel] = ImageToolInput

    _client: InferenceClient = PrivateAttr()

    def __init__(self):
        super().__init__()
        hf_token = os.environ.get("HF_TOKEN")
        if not hf_token:
            raise ValueError("HF_TOKEN environment variable not set.")
        self._client = InferenceClient(token=hf_token)

    def _run(self, prompt: str) -> str:
        """Generate an image and save it locally."""
        try:
            # Clean the prompt - remove problematic characters
            clean_prompt = re.sub(r"[\\'\"]", "", prompt)
            clean_prompt = clean_prompt[:500]  # Limit length
            
            # Generate image using Hugging Face text-to-image
            image = self._client.text_to_image(
                prompt=clean_prompt,
                model="stabilityai/stable-diffusion-xl-base-1.0",
            )

            # Ensure folder exists
            os.makedirs("generated_images", exist_ok=True)
            filename = f"blog_{uuid.uuid4().hex[:8]}.png"
            filepath = os.path.join("generated_images", filename)
            image.save(filepath)

            return f"Image saved at: {filepath}"

        except Exception as e:
            return f"Error generating image: {str(e)}"