# Ejemplo con pytesseract

import pytesseract
import cv2
from dotenv import load_dotenv
import os
from pypdf import PdfReader
import io
from PIL import Image

load_dotenv()

# path_exe = os.getenv("TESSERACT_CMD")

# pytesseract.pytesseract.tesseract_cmd = path_exe




def find_tesseract():
    default_path = os.path.expanduser(r'~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe')
    if os.path.exists(default_path):
        return default_path
    return None

path_exe = find_tesseract()

if not path_exe:
    # Ejecutar el script de instalación de Tesseract
    os.system("powershell -ExecutionPolicy Bypass -File install_tesseract.ps1")
    path_exe = find_tesseract()


pytesseract.pytesseract.tesseract_cmd = path_exe

print(f"Path Exe: {path_exe}")

def extract_data_from_image(path_file):

    grey_image = cv2.imread(path_file, cv2.IMREAD_GRAYSCALE)

    _, th = cv2.threshold(grey_image, 138,255,cv2.THRESH_BINARY)

    #cv2.imshow("Ti", th)
    #cv2.waitKey(0)
    text = pytesseract.image_to_string(th)
    print(text)

    return text

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = reader.pages[0].extract_text()  # Leer solo la primera página
        print("Texto del pdf: ", text)
        return text
    
# Funcion para extraer imagenes de un pdf
def extract_imagenes_pdf(file):
    reader = PdfReader(file)
    image_list = []

    for page_num, page in enumerate(reader.pages):
        for image_index, image_file_object in enumerate(page.images):
            image_bytes = image_file_object.data
            image_ext = image_file_object.name.split('.')[-1]
            image = Image.open(io.BytesIO(image_bytes))
            image_list.append((image, image_ext))

    return image_list


# Mantener la consola abierta
#input("Presiona Enter para salir...")