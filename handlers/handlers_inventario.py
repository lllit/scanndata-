from utils.exportacion import PDF
import pandas as pd

def on_save_location_selected_pdf(e, page,data):
    from datetime import datetime
    if e.path:
        folder_path = e.path
        print(folder_path)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"{folder_path}/db_inventario_{now}.pdf"
        #ave_pdf(path=file_path)

        pdf = PDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        column_widths = [40, 40, 40]
        header = ["Producto", "Precio", "Stock"]
        for i, col_name in enumerate(header):
            pdf.cell(column_widths[i], 10, col_name, 1, 0, "C")
        pdf.ln()
        data_ = data.get_all_values()
        for row in data_:
            pdf.cell(column_widths[0], 10, row["Producto"], 1)
            pdf.cell(column_widths[1], 10, str(row["Precio"]), 1)
            pdf.cell(column_widths[2], 10, str(row["Stock"]), 1)
            pdf.ln()

        # Save the PDF
        pdf.output(file_path)

        

        print("Guardado exitosamente")
        page.update()
    
def on_save_location_selected_excel(e,page,data):
    from datetime import datetime
    if e.path:
        folder_path = e.path
        #print(folder_path)
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = f"{folder_path}/db_inventario_{now}.xlsx"
        data_ = data.get_all_values()
        df = pd.DataFrame(data_, columns=["Producto", "Precio", "Stock"])
        df.to_excel(file_path, index=False)
        
        print("Guardado exitosamente")
        page.update()


    
def on_export_click_pdf(e,file_picker_pdf):
    file_picker_pdf.get_directory_path()
    
def on_export_click_excel(e,file_picker_excel):
    file_picker_excel.get_directory_path()
    
    