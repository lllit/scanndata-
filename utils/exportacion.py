
import pandas as pd

from pypdf import PdfWriter, PageObject
from fpdf import FPDF

from docx2pdf import convert
import fitz

from docx import Document
import csv

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

## COVERTER 

def export_docx_to_csv(docx_filename, csv_filename):
    # Leer el archivo DOCX
    doc = Document(docx_filename)
    
    # Abrir el archivo CSV para escribir
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Iterar a través de cada párrafo en el archivo DOCX
        for para in doc.paragraphs:
            # Escribir cada párrafo como una fila en el archivo CSV
            writer.writerow([para.text])


    
def export_csv_to_pdf(csv_filename, pdf_filename):
    # Leer el archivo CSV
    df = pd.read_csv(csv_filename)
    
    # Crear un objeto PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Establecer la fuente
    pdf.set_font("Arial", size = 12)
    
    # Añadir una celda
    for i in range(len(df)):
        row = df.iloc[i]
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln()
    
    # Guardar el PDF en un archivo
    pdf.output(pdf_filename)




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



def export_docx_to_pdf(docx_filename, pdf_filename):
    
    convert(input_path=docx_filename,output_path=pdf_filename)