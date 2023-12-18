import pytesseract
from PIL import Image

image = Image.open("ocr_hindi_image.png")

text = pytesseract.image_to_string(image, lang="hin")
print(text)
#this code demonstrates the use of Tesseract Library
