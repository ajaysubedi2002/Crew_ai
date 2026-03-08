import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env file
load_dotenv()

def test_hf_model_direct(prompt: str):
    token = os.environ.get("HF_TOKEN")
    print(f"Token present: {bool(token)}")
    print(f"Token starts with: {token[:10] if token else 'N/A'}...")
    
    # Use HF token directly - no provider
    client = InferenceClient(token=token)

    print(f"Testing model with prompt: {prompt}")
    try:
        # Use a free model on HF Inference API
        image = client.text_to_image(
            prompt,
            model="stabilityai/stable-diffusion-xl-base-1.0",
        )
        
        # Save and show for immediate feedback
        image.save("quick_test.png")
        image.show() 
        print("Success! Image saved as quick_test.png")
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    test_hf_model_direct("A minimalist 3D isometric office icon, high resolution")