import google.generativeai as genai
from PIL import Image

# 🔑 Configure API
genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your Gemini API key

# Text response
def get_text_response(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text

# Image understanding
def analyze_image(image_path, user_prompt="Describe this image."):
    model = genai.GenerativeModel("gemini-1.5-pro-vision")
    with open(image_path, "rb") as img:
        response = model.generate_content([user_prompt, img])
    return response.text

# Image generation (placeholder using text response)
def generate_image(prompt, filename="generated.png"):
    # NOTE: Gemini currently supports image *understanding*; 
    # for image *generation*, use Imagen API (if available).
    # Here, we simulate image generation by saving text as an image.
    from PIL import ImageDraw
    img = Image.new("RGB", (600, 200), color="white")
    d = ImageDraw.Draw(img)
    d.text((10, 80), f"Generated: {prompt}", fill=(0, 0, 0))
    img.save(filename)
    return filename
