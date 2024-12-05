from ocr_easy import easy_extract
from ocr_tesseract import tesseract_extract


def main():
    image_path = "example_images/example2.png"

    # languages: rus, eng, rus+eng
    text = tesseract_extract(image_path=image_path, lang="rus")
    with open("tesseract_output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # languages: https://github.com/JaidedAI/EasyOCR/tree/master/easyocr/character
    text = easy_extract(image_path=image_path, lang="ru")
    with open("easy_output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print(text)


if __name__ == "__main__":
    main()
