import flet as ft
from utils.constantes import *
from assets.styles.styles import colors



menubartabla = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.ColorScheme(ft.Colors.AMBER),
            padding=ft.padding.all(10)
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Archivo"),
                controls=[],
            ),
            ft.SubmenuButton(
                content=ft.Text("BD Opciones"),
                controls=[],
            ),
        ],
    )