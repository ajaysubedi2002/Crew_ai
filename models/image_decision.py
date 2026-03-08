from pydantic import BaseModel, Field
from typing import List

class ImageDecision(BaseModel):
    """Structured output for image decisions"""

    generate_images: bool = Field(
        description="Whether images should be included in the blog"
    )

    image_sections: List[str] = Field(
        description="List of section titles where images should be inserted"
    )

    image_prompts: List[str] = Field(
        description="Prompts describing what image should be generated for each section"
    )