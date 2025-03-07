import flet as ft
from handlers.handlers_navegacion import cambiar_pagina



def nav_bar(page):

    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.DOCUMENT_SCANNER,label="Extracción"),
            ft.NavigationBarDestination(icon=ft.Icons.TABLE_CHART,label="Tablas"),
            ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH,label="Calendario"),
        ],
        on_change=lambda e: cambiar_pagina(index=e.control.selected_index, page=page),
        bgcolor=ft.Colors.BLACK12
    )

    return nav_bar

