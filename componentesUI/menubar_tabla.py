import flet as ft
from utils.constantes import *
from assets.styles.styles import colors


# Menu de tablas
menubartabla = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor={
                ft.ControlState.HOVERED: ft.Colors.WHITE,
                ft.ControlState.FOCUSED: ft.Colors.BLUE,
                ft.ControlState.DEFAULT: colors[1],
            },
            padding=ft.padding.all(10)
        ),
        controls=[
            ft.SubmenuButton(
                style=ft.ButtonStyle(bgcolor=colors[1]),
                content=ft.Text("Archivo"),
                controls=[],
            ),
            ft.SubmenuButton(
                content=ft.Text("BD Opciones"),
                controls=[],
            ),
        ],
    )