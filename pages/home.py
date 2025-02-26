import flet as ft

from assets.styles.styles import PADDING_TOP


def saludo_bienvenida():
    return ft.Column(
        controls=[
            ft.Text("¡Hola!", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
            ft.Text("Bienvenido para extraer información", size=20)
        ], 
        
        alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

def HomePage():
    return ft.Container(
        content=(
            saludo_bienvenida()
        ),
        padding=ft.padding.only(top=PADDING_TOP)

    )