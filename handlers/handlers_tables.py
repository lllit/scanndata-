from utils.tabla_utils import load_data,update_table
from utils.exportacion import export_data_to_csv
from utils.dialog import opendialog

def on_sheet_selected(e,page,current_google_sheet,table,titulo_hoja,current_sheet_name,file_name_gs,gs):
    new_current_sheet_name = e.control.content.value
    

    print(f"ON SHEET SELECT {new_current_sheet_name}")
    update_table(page,current_google_sheet,new_current_sheet_name, table,titulo_hoja,current_sheet_name,file_name_gs,gs)


def on_save_location_selected(e, gs,fecha_exportacion,page):
    if e.path:
        folder_path = e.path
        
        data = gs.get_all_values()
        export_data_to_csv(data, f"{folder_path}\\{fecha_exportacion}_data.csv")
        page.open(opendialog(page, "Datos exportados a CSV", f"Guardados en: {folder_path}\\{fecha_exportacion}_data.csv"))
        page.update()