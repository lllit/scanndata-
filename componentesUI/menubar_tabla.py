import flet as ft
from utils.constantes import *




menubartabla = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.Colors.BLACK12,
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