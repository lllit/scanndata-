import flet as ft

def HomePage():
    return ft.Column([
        ft.Text("¡Hola!", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700),
        ft.Text("Bienvenido para extraer información", size=20)
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)