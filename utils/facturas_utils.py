import flet as ft
import shutil
import zipfile
import os

from utils.exportacion import export_docx_to_pdf, pdf_to_image


def generar_factura(page,datos, factura_preview):
    try:
        shutil.copytree("./plantillas/plantilla","./plantillas/documento_tmp")
        with open("./plantillas/plantilla/word/document.xml", "r") as file:
            data = file.read()
            for key, value in datos.items():
                data= data.replace(key,value)   
        with open("./plantillas/documento_tmp/word/document.xml", "w") as file:
            file.write(data)

        with zipfile.ZipFile("./plantillas/factura_final.docx", 'w') as zipf:
            for root, dirs, files in os.walk("./plantillas/documento_tmp"):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "./plantillas/documento_tmp"))   
        shutil.rmtree("./plantillas/documento_tmp")
        export_docx_to_pdf("./plantillas/factura_final.docx", "./plantillas/factura_final.pdf") 
        pdf_to_image("./plantillas/factura_final.pdf","./plantillas/factura_final_imagen.png")  
        factura_preview.src = "./plantillas/factura_final_imagen.png"
        page.update()   
        print("Factura generada")   
    except Exception as e:
        print("error ", e)