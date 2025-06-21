# Import the pytesseract library for OCR (Optical Character Recognition)
import pytesseract
# Import the os module (not used currently, but often useful for file handling)
import os
# Import the Image class from PIL (Python Imaging Library) to work with images
from PIL import Image

# Set the path to the Tesseract executable on your system
# This allows pytesseract to find and use Tesseract
pytesseract.pytesseract.tesseract_cmd = r"F:\Tesseract\tesseract" # Path to the tesseract

def convert():
    try:
        # Attempt to open the image file for reading
        image = Image.open('image-to-text\Capture.JPG')
    except FileNotFoundError:
        print("Error: The image file was not found. Please check the path.")
        return
    except Exception as e:
        print(f"Unexpected error while opening the image: {e}")
        return
    
    try:
        # Attempt to extract text from the image using pytesseract with English language
        text = pytesseract.image_to_string(image, lang='eng')
        print("Extracted Text:\n", text)
    except pytesseract.TesseractNotFoundError:
        print("Error: Tesseract executable not found. Please check the path.")
    except Exception as e:
        print(f"Unexpected error during text extraction: {e}")

convert()