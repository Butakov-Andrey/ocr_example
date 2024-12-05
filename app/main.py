from ocr_easy import easy_extract
from ocr_tesseract import tesseract_extract


def main():
    image_path = "example_images/example3.JPG"

    # languages: rus, eng, rus+eng
    # text = tesseract_extract(image_path=image_path, lang="eng")

    # languages: https://github.com/JaidedAI/EasyOCR/tree/master/easyocr/character
    text = easy_extract(image_path=image_path, lang="en")

    print(text)


if __name__ == "__main__":
    main()
