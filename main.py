import flet as ft
import os
import subprocess

from pages.home import HomePage
from pages.extraccion_page import ExtractPage
from pages.extraccion_imagenes_pdf import ExtractImgPage
from pages.tables_view import TablesPage

from utils.openmenu import create_navigation_drawer,open_menu_lateral

def main(page: ft.Page):
    page.title = "ScannData 0.1"
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

    drawer = create_navigation_drawer(page, cambiar_pagina)
    page.appbar = ft.AppBar(
        title=ft.Text("ScannData", weight=ft.FontWeight.W_500),
        leading=open_menu_lateral(page, drawer),
        title_spacing=ft.padding.only(top=3)
    )

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




if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")