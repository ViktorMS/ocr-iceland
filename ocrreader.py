try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseractpath = r'C:\Users\User\AppData\Local\Tesseract-OCR\tesseract.exe'
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = pytesseractpath
path = r'C:\Users\User\Desktop\screenshot1.png'

# Simple image to string
islstring = pytesseract.image_to_string(Image.open(path), lang="isl")
print(islstring)
