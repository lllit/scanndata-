import flet as ft
from utils.constantes import *
from assets.styles.styles import *

from utils.google_sheets_actions import GoogleSheet



def TablesPage(page):
    titulo = ft.Text(f"Tabla {sheet_name}", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)


    gs = GoogleSheet(file_name_gs, google_sheet, sheet_name)

    # Obtén todos los valores de la hoja
    data = gs.get_all_values()

    #print("DATA: ",data)
    rows = [
        ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(row["rut_emisor"])),
                ft.DataCell(ft.Text(row["razon_social_emisor"])),
                ft.DataCell(ft.Text(row["folio_dte"])),
                ft.DataCell(ft.Text(row["fecha_factura_boleta"])),
                ft.DataCell(ft.Text(row["monto"])),
                ft.DataCell(ft.Text(row["primer_item"])),
            ],
        ) for row in data
    ]

    return ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                ft.DataTable(
                    
                    columns=[
                        ft.DataColumn(ft.Text("RUT Emisor",max_lines=2, no_wrap=True)),
                        ft.DataColumn(ft.Text("Razón Social Emisor",max_lines=2, no_wrap=True)),
                        ft.DataColumn(ft.Text("Folio DTE",max_lines=2, no_wrap=True)),
                        ft.DataColumn(
                            ft.Text("Fecha Factura/Boleta",max_lines=2, no_wrap=True)
                            
                        ),
                        ft.DataColumn(ft.Text("Monto",max_lines=2, no_wrap=True), numeric=True),
                        ft.DataColumn(ft.Text("Primer Ítem",max_lines=2, no_wrap=True)),
                    ],
                    rows=rows,
                    horizontal_lines=ft.BorderSide(1,"gray"),
                    vertical_lines=ft.BorderSide(1, "gray"),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.only(top=PADDING_TOP)
    )
