import pytesseract
from PIL import Image


def tesseract_extract(image_path: str, lang: str):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(image=img, lang=lang)
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
