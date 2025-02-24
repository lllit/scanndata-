import flet as ft


from pages.home import HomePage
from pages.extraccion_page import ExtractPage
from pages.extraccion_imagenes_pdf import ExtractImgPage


def main(page: ft.Page):
    page.title = "Extracción de data"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO


    def cambiar_pagina(e):
        if e.control.selected_index == 0:
            page.controls[1] = HomePage()
        elif e.control.selected_index == 1:
            page.controls[1] = ExtractPage(page)
        elif e.control.selected_index == 2:
            page.controls[1] = ExtractImgPage(page)
        page.update()


    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.DATA_EXPLORATION, label="Función Extract"),
            ft.NavigationBarDestination(icon=ft.Icons.DATA_ARRAY, label="Extraccion de imagenes en pdf"),
        ],
        on_change=cambiar_pagina,
        bgcolor=ft.Colors.BLACK12
    )

    # Configurar UI
    page.add(
        nav_bar
    )
    page.add(
        HomePage()
    )

    page.update()



ft.app(target=main,assets_dir="assets")

if __name__ == "__main__":
    ft.Window(
        title="Extracción de data",
        target=main,
        assets_dir="assets",
        icon="assets/favicon.ico"
    ).run()