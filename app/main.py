from ocr_tesseract import extract_text_from_image


def main():
    image_path = "example_images/example1.png"

    # languages: rus, eng, rus+eng
    text = extract_text_from_image(image_path=image_path, lang="eng")
    print(text)


if __name__ == "__main__":
    main()
