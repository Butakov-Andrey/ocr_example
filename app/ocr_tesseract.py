import pytesseract
from PIL import Image


def extract_text_from_image(image_path: str, lang: str):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(image=img, lang=lang)
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
