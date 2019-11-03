# OCR read contents of clipboard and save to file

from PIL import ImageGrab

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Install Tesseract-OCR https://github.com/UB-Mannheim/tesseract/wiki
# with additional Icelandic language package
# Put this script in the same folder
#   \
#   ↳ This_Script.py
#   ↳ Tesseract-OCR \ tesseract.exe

pytesseractpath = r"Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = pytesseractpath

im = ImageGrab.grabclipboard()

if isinstance(im, Image.Image):
    im.save('ocr.png')
    islstring = pytesseract.image_to_string('ocr.png', lang="isl")
    print(islstring)
    with open("ocr.txt", "w") as text_file:
        print(f"{islstring}", file=text_file)
else:
    print('No image in clipboard')
