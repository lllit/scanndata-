import flet as ft



def create_navigation_drawer(page, cambiar_pagina):
    return ft.NavigationDrawer(
        on_dismiss=None,
        on_change=lambda e: cambiar_pagina(e.control.selected_index,page),
        controls=[
            ft.Container(height=12, 
                        padding=ft.padding.only(top=30)
            ),
            ft.NavigationDrawerDestination(
                label="Home",
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.HOME),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.DOCUMENT_SCANNER_OUTLINED),
                label="Extracción",
                selected_icon=ft.Icons.DOCUMENT_SCANNER,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.TABLE_CHART_OUTLINED),
                label="Tablas",
                selected_icon=ft.Icons.TABLE_CHART,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.CALENDAR_MONTH),
                label="Calendario",
                selected_icon=ft.Icons.CALENDAR_MONTH,
            ),
        ],
        bgcolor=ft.Colors.BLACK54
    )

def open_menu_lateral(page,drawer):
    return ft.IconButton(
        icon=ft.Icons.MENU,
        on_click=lambda e: page.open(drawer),
        tooltip="Menú"
    )
