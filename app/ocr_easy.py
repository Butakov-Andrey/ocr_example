import easyocr


def easy_extract(image_path: str, lang: str):
    try:
        reader = easyocr.Reader([lang])
        result = reader.readtext(image_path, detail=0)
        text = "\n".join(result)

        return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
