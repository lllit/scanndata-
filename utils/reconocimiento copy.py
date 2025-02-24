# Ejemplo con pytesseract

import pytesseract
import cv2
from dotenv import load_dotenv
import os

load_dotenv()
path_exe = os.getenv("TESSERACT_CMD")

pytesseract.pytesseract.tesseract_cmd = path_exe



grey_image = cv2.imread("data/factura.png", cv2.IMREAD_GRAYSCALE)
_, th = cv2.threshold(grey_image, 138,255,cv2.THRESH_BINARY)
#cv2.imshow("Ti", th)
#cv2.waitKey(0)
text = pytesseract.image_to_string(th)
print(text)

