import flet as ft
import gspread

from utils.google_sheets_actions import GoogleSheet, GoogleSheetGeneral

from utils.constantes import *
from assets.styles.styles import *


current_google_sheet = google_sheet[0]

gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
all_sheets = gs_general.get_all_sheets()
#print(all_sheets)
current_sheet_name = all_sheets[0]
gs = GoogleSheet(file_name_gs, current_google_sheet, current_sheet_name)


def load_data(google_sheet, new_current_sheet_name,file_name_gs,gs):
    #print("LOAD DATA "+google_sheet)
    

    try:
        
        gs_general = GoogleSheetGeneral(file_name_gs, google_sheet)
        all_sheets = gs_general.get_all_sheets()
        #print("all_sheets "+all_sheets[0])
        
        
        #print("LOAD current_sheet_name ", current_sheet_name)
        #print("LOAD new_current_sheet_name ", new_current_sheet_name)

        gs.sheet = gs.sh.worksheet(new_current_sheet_name)
 
    except gspread.exceptions.WorksheetNotFound:
        #print(f"Worksheet '{current_sheet_name}' not found.")
        return [], []
    
    
    data = gs.get_all_values()

    

    if not data:
        return [], []
    
    columns = [ft.DataColumn(ft.Text(col)) for col in data[0].keys()]

    rows = [
        ft.DataRow(
            cells=[ft.DataCell(ft.Text(str(value))) for value in row.values()]
        ) for row in data
    ]

    

    return columns, rows


def update_table(page,google_sheet,new_current_sheet_name,table,titulo_hoja,current_sheet_name,file_name_gs,gs):
        
    columns, rows = load_data(google_sheet,new_current_sheet_name,file_name_gs,gs)

    if not columns:
        columns = [ft.DataColumn(ft.Text("Sin información"))]
        rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(f"No hay data en la hoja: {current_sheet_name}")
                    )
                ]
            )
        ]

    table.columns = columns
    table.rows = rows

    titulo_hoja.value = google_sheet

    page.update()

def on_database_selected(page,
                        google_sheet,
                        current_google_sheet,
                        gs,current_sheet_name, 
                        file_name_gs,
                        table,
                        titulo_hoja,
                        on_sheet_selected,
                        menubartabla):
    #nonlocal current_google_sheet, gs, current_sheet_name
    try:
        #print(f"GoogleSheet {google_sheet}")
        current_google_sheet = google_sheet 
        
        gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
        all_sheets = gs_general.get_all_sheets()
        #print("on_database_selected all_sheets ",all_sheets[0])
        gs = GoogleSheet(file_name_gs, current_google_sheet, all_sheets[0])
        
        
        update_table(page,current_google_sheet, all_sheets[0], table,titulo_hoja,current_sheet_name,file_name_gs,gs)

        sheet_menu_items = [
            ft.MenuItemButton(
                content=ft.Text(sheet),
                on_click=lambda _: on_sheet_selected(page,
                                                     current_google_sheet,
                                                     table,
                                                     titulo_hoja,
                                                     current_sheet_name,
                                                     file_name_gs,
                                                     gs),
                
            ) for sheet in all_sheets
        ]
        menubartabla.controls[1].controls = sheet_menu_items
        page.update()
    except gspread.exceptions.WorksheetNotFound:
        print(f"Database '{current_sheet_name}' not found.")

