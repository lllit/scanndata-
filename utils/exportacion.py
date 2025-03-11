
import pandas as pd

from pypdf import PdfWriter, PageObject
from fpdf import FPDF

from docx2pdf import convert
import fitz


def export_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def export_data_to_pdf(data, filename):
    pdf_writer = PdfWriter()
    page = PageObject.create_blank_page(width=210, height=297)  # A4 size in mm

    # Add table headers
    headers = data[0].keys()
    y_position = 280  # Start position from the top
    for header in headers:
        page.insert_text(header, x=10, y=y_position)
        y_position -= 10

    # Add table rows
    for row in data:
        y_position -= 10
        for value in row.values():
            page.insert_text(str(value), x=10, y=y_position)
            y_position -= 10

    pdf_writer.add_page(page)
    with open(filename, "wb") as f:
        pdf_writer.write(f)

def export_docx_to_pdf(docx_filename, pdf_filename):
    
    convert(input_path=docx_filename,output_path=pdf_filename)
    


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0,10,"Inventario", 0,1,"C")
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0,10,f"Pagina {self.page_no()}",0,0,"C")

def pdf_to_image(pdf_path, output_path):
    # Abrir el documento PDF
    pdf_document = fitz.open(pdf_path)

    # Seleccionar la primera página
    page = pdf_document.load_page(0)

    # Renderizar la página a una imagen
    pix = page.get_pixmap()

    # Guardar la imagen
    pix.save(output_path)