
import pandas as pd
from pypdf import PdfWriter, PageObject



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