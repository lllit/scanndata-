import flet as ft
import os
import subprocess

from pages.home import HomePage
from pages.extraccion_page import ExtractPage
from pages.extraccion_imagenes_pdf import ExtractImgPage
from pages.tables_view import TablesPage



def main(page: ft.Page):
    page.title = "ExtData 0.1"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO


    global cambiar_pagina

    def cambiar_pagina(index):
        if index == 0:
            page.controls[1] = HomePage(page)
        elif index == 1:
            page.controls[1] = ExtractPage(page,cambiar_pagina)
        elif index == 2:
            page.controls[1] = TablesPage(page)
        elif index == 3:
            page.controls[1] = ExtractImgPage(page)
        page.update()


    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.DOCUMENT_SCANNER,label="Lector IMG/PDF"),
            ft.NavigationBarDestination(icon=ft.Icons.TABLE_CHART,label="Tablas"),
            ft.NavigationBarDestination(icon=ft.Icons.TRANSFORM,label="Imagen a pdf"),
        ],
        on_change=lambda e: cambiar_pagina(e.control.selected_index),
        bgcolor=ft.Colors.BLACK12
    )

    # Configurar UI
    page.add(
        nav_bar
    )
    page.add(
        HomePage(page)
    )

    page.update()



#ft.app(target=main,assets_dir="assets")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")