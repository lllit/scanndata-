import flet as ft
from datetime import date
import gspread

from utils.constantes import *
from assets.styles.styles import *

from utils.google_sheets_actions import GoogleSheet, GoogleSheetGeneral
from utils.exportacion import export_data_to_csv,export_data_to_pdf
from utils.dialog import opendialog


from componentesUI.menubar_tabla import menubartabla


URL_EXPORT = "files_export/"


def TablesPage(page):

    

    titulo = ft.Text(f"Tabla de datos", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)

    current_google_sheet = google_sheet[0]

    gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
    all_sheets = gs_general.get_all_sheets()
    print(all_sheets)

    current_sheet_name = all_sheets[0]
    gs = GoogleSheet(file_name_gs, current_google_sheet, current_sheet_name)


    print(f"Current {current_google_sheet}")
    

    # --------------------------------------------

    def load_data(google_sheet, new_current_sheet_name):
        print("LOAD DATA "+google_sheet)

        try:
            
            gs_general = GoogleSheetGeneral(file_name_gs, google_sheet)
            all_sheets = gs_general.get_all_sheets()
            print("all_sheets "+all_sheets[0])
            current_sheet_name = all_sheets[0]
            
            
            #current_sheet_name = new_current_sheet_name
            print("LOAD current_sheet_name ", current_sheet_name)
            print("LOAD new_current_sheet_name ", new_current_sheet_name)

            gs.sheet = gs.sh.worksheet(new_current_sheet_name)
 
        except gspread.exceptions.WorksheetNotFound:
            print(f"Worksheet '{current_sheet_name}' not found.")
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

        

    def update_table(google_sheet,new_current_sheet_name):
        
        columns, rows = load_data(google_sheet,new_current_sheet_name)

        if not columns:
            columns = [ft.DataColumn(ft.Text("Sin información"))]
            rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(f"No hay data en la hoja: {current_sheet_name}"))])]

        table.columns = columns
        table.rows = rows
        page.update()



    def on_sheet_selected(e):
        new_current_sheet_name = e.control.content.value
        

        print(f"ON SHEET SELECT {new_current_sheet_name}")
        update_table(current_google_sheet,new_current_sheet_name)


    def on_database_selected(google_sheet):
        nonlocal current_google_sheet, gs, current_sheet_name
        try:
            print(f"GoogleSheet {google_sheet}")
            current_google_sheet = google_sheet 
            
            gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
            all_sheets = gs_general.get_all_sheets()
            print("on_database_selected all_sheets ",all_sheets[0])
            gs = GoogleSheet(file_name_gs, current_google_sheet, all_sheets[0])
            
            
            update_table(current_google_sheet, all_sheets[0])

            sheet_menu_items = [
                ft.MenuItemButton(
                    content=ft.Text(sheet),
                    on_click=on_sheet_selected
                ) for sheet in all_sheets
            ]
            menubartabla.controls[1].controls = sheet_menu_items
            page.update()
        except gspread.exceptions.WorksheetNotFound:
            print(f"Database '{current_sheet_name}' not found.")


    database_menu_items = [
        ft.MenuItemButton(
            content=ft.Text(sheet),
            on_click=lambda e, sheet=sheet: on_database_selected(sheet)
        ) for sheet in google_sheet
    ]

    

    menubartabla.controls[0].controls = database_menu_items


    sheet_menu_items = [
        ft.MenuItemButton(
            content=ft.Text(sheet),
            on_click=on_sheet_selected,
        
        ) for sheet in all_sheets
    ]

    menubartabla.controls[1].controls = sheet_menu_items
    



    initial_columns, initial_rows = load_data(current_google_sheet, current_sheet_name)

    if not initial_columns:
        initial_columns = [ft.DataColumn(ft.Text("Sin información"))]
        initial_rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(f"No hay data en la hoja: {current_sheet_name}"))])]

    table = ft.DataTable(
        columns=initial_columns,
        rows=initial_rows,
        horizontal_lines=ft.BorderSide(1,"gray"),
        vertical_lines=ft.BorderSide(1, "gray"),
        bgcolor=ft.Colors.with_opacity(0.4,colors[1]),
        border_radius=ft.border_radius.all(10)
    )
    scrollable_table = ft.Row(
        controls=[table],
        scroll=ft.ScrollMode.AUTO
    )

    # --------------------------------------------
    fecha_exportacion = date.today()

    def on_save_location_selected(e):
        if e.path:
            folder_path = e.path
            data = gs.get_all_values()
            export_data_to_csv(data, f"{folder_path}\\{fecha_exportacion}_data.csv")
            page.open(opendialog(page, "Datos exportados a CSV", f"Guardados en: {folder_path}\\{fecha_exportacion}_data.csv"))
            page.update()

    
    file_picker = ft.FilePicker(on_result=on_save_location_selected)
    page.overlay.append(file_picker)

    def on_export_click(e):
        file_picker.get_directory_path()


    
    def open_edit_dialog(row_data):
        """
        Editar datos de la tabla y directamente en la base de datos
        """ 
        def on_save_click(e):
            gs.write_data_by_uid(row_data["uid"], [
                rut_emisor.value, 
                razon_social_emisor.value, 
                folio_dte.value, 
                fecha_factura_boleta.value, 
                monto.value, 
                primer_item.value
            ])
            page.open(opendialog(page,"Datos actualizados!","Datos actualizados!"))
            page.close(dlg)
            update_table()

        rut_emisor = ft.TextField(label="RUT Emisor", value=row_data["rut_emisor"])
        razon_social_emisor = ft.TextField(label="Razón Social Emisor", value=row_data["razon_social_emisor"])
        folio_dte = ft.TextField(label="Folio DTE", value=row_data["folio_dte"])
        fecha_factura_boleta = ft.TextField(label="Fecha Factura/Boleta", value=row_data["fecha_factura_boleta"])
        monto = ft.TextField(label="Monto", value=row_data["monto"])
        primer_item = ft.TextField(label="Primer Ítem", value=row_data["primer_item"])
        

        dlg = ft.AlertDialog(
            title=ft.Text("Editar Datos"),
            content=ft.Column([
                rut_emisor,
                razon_social_emisor,
                folio_dte,
                fecha_factura_boleta,
                monto,
                primer_item
            ]),
            actions=[
                ft.TextButton("Guardar", on_click=on_save_click),
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.close(dlg)
        )
        page.open(dlg)
        page.update()
        update_table(gs.sheet.title)



    def open_delete_dialog(row_data):
        def on_delete_click(e):
            # Elimina los datos en Google Sheets
            gs.delete_row_by_uid(row_data["uid"])
            page.open(opendialog(page, "Datos eliminados!", "Datos eliminados!"))
            page.close(dlg)
            update_table()

        dlg = ft.AlertDialog(
            title=ft.Text("¿Estas seguro de eliminar?"),
            actions=[
                ft.TextButton("Eliminar", on_click=on_delete_click),
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: page.close(dlg)
        )
        page.open(dlg)
        page.update()


    
    

    

    ui_principal = ft.Column(
        controls=[
            scrollable_table,
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.DOWNLOAD,
                            on_click=on_export_click,
                            tooltip="Exportar datos a CSV"
                        ),
                    ],
                    
                    alignment=ft.MainAxisAlignment.END
                ),
                padding=ft.padding.only(right=30)
            ),
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row([menubartabla]),
                ui_principal,
            ],
        ),
        padding=ft.padding.only(top=PADDING_TOP)
    )

