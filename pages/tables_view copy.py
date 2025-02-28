import flet as ft
from datetime import date

from utils.constantes import *
from assets.styles.styles import *

from utils.google_sheets_actions import GoogleSheet
from utils.exportacion import export_data_to_csv,export_data_to_pdf
from utils.dialog import opendialog


from componentesUI.menubar_tabla import menubartabla


URL_EXPORT = "files_export/"


def TablesPage(page):
    titulo = ft.Text(f"Tabla de datos", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    
    sheet_name = "facturas_boletas"    

    gs = GoogleSheet(file_name_gs, google_sheet, sheet_name)

    all_sheets = gs.get_all_sheets()
    #print(all_sheets)



    def load_data():
        # Obtén todos los valores de la hoja
        data = gs.get_all_values()
        rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row["rut_emisor"])),
                    ft.DataCell(ft.Text(row["razon_social_emisor"])),
                    ft.DataCell(ft.Text(row["folio_dte"])),
                    ft.DataCell(ft.Text(row["fecha_factura_boleta"])),
                    ft.DataCell(ft.Text(row["monto"])),
                    ft.DataCell(ft.Text(row["primer_item"])),
                    ft.DataCell(ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, row=row: open_edit_dialog(row)),
                            ft.IconButton(icon=ft.Icons.DELETE, on_click=lambda e, row=row: open_delete_dialog(row), icon_color=ft.Colors.RED_400)
                        ]
                    ))
                ],
            ) for row in data
        ]
        return rows

    def update_table():
        table.rows = load_data()
        page.update()

    

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



    table = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("RUT Emisor",max_lines=2, no_wrap=True)),
                    ft.DataColumn(ft.Text("Razón Social Emisor",max_lines=2, no_wrap=True)),
                    ft.DataColumn(ft.Text("Folio DTE",max_lines=2, no_wrap=True)),
                    ft.DataColumn(
                        ft.Text("Fecha Factura/Boleta",max_lines=2, no_wrap=True)
                        
                    ),
                    ft.DataColumn(ft.Text("Monto",max_lines=2, no_wrap=True), numeric=True),
                    ft.DataColumn(ft.Text("Primer Ítem",max_lines=2, no_wrap=True)),
                    ft.DataColumn(ft.Text("Acciones", max_lines=2, no_wrap=True))
                ],
                rows=load_data(),
                horizontal_lines=ft.BorderSide(1,"gray"),
                vertical_lines=ft.BorderSide(1, "gray"),
            )

    

    ui_principal = ft.Column(
        controls=[
            titulo,
            
            table,
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

