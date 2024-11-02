# import necessary packages
import pathlib
import textwrap
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to display text in markdown format
def to_markdown(text):
    text = text.replace('~', '*')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Setup your API key
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the API key
genai.configure(api_key=api_key)

# Using the 'gemini-pro' model for text-based prompts
model = genai.GenerativeModel('gemini-pro')

# Generate text from a prompt
text_to_text = "How to boost our cloth business on social media as a advertisement"
print('\r')
print(text_to_text)
print('\r')
response = model.generate_content(text_to_text)

# Check for a valid response
if hasattr(response, 'text'):
    print(to_markdown(response.text))
else:
    print("No valid response generated, possibly due to copyright concerns.")

# Generate text from an image input
img = Image.open('images.jpeg')  # Update the image path to your local file path

# Use the 'gemini-1.5-flash' model for image-based prompts
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content(img)

# Check for a valid response for image-based input
if hasattr(response, 'text'):
    print('\r')
    print("Image to text Generation")
    print('\r')
    print(to_markdown(response.text))
    print('\r')
else:
    print("No valid response generated for the image input, possibly due to copyright concerns.")

# Generate text from both text and image
response = model.generate_content(
    ["Write a short, engaging blog post based on this picture. It should include a description of the photo", img],
    stream=True
)
response.resolve()

# Check for a valid response when using both text and image inputs
if hasattr(response, 'text'):
    print("\r")
    print("\r")
    print("Text Generation by image and text")
    print("\r")
    print(to_markdown(response.text))
else:
    print("No valid response generated for the combined text and image input.")
