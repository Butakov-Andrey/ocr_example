# OCR Example

## TesseractOcr
Простой пример распознавания текста с помощью pytesseract.  
Используется Docker контейнер, т.к. pytesseract требует системные пакеты:
```
tesseract-ocr \
tesseract-ocr-rus \
tesseract-ocr-eng \
```

## Начало работы
Запуск Docker контейнера:
```
docker-compose up -d --build
```