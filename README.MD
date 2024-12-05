# OCR Example

## TesseractOcr
Пример распознавания текста с помощью pytesseract.  
Используется Docker контейнер, т.к. pytesseract требует системные пакеты в зависимости от необходимых языков:
```
tesseract-ocr \
tesseract-ocr-rus \
tesseract-ocr-eng \
```

## EasyOcr
Пример распознавания текста с помощью easyocr.  

## Начало работы
Запуск Docker контейнера:
```
docker-compose up -d --build
```