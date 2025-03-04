import flet as ft
from utils.constantes import *
from assets.styles.styles import colors



menubartabla = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=colors[0],
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