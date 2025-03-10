import flet as ft

from componentesUI.railFacturas import railFacturas
from pages.extraccion_imagenes_pdf import PADDING_TOP

def FacturasEditPage(page):
    return ft.Container(
        padding=ft.padding.only(top=PADDING_TOP),
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    content=railFacturas(page)
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.top_center,
                    content=ft.Text("Facturas Edit")
                )
            ]
        )
    )