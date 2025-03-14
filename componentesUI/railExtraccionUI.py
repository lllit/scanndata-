import flet as ft




def railExtraccionPage(page):

    from handlers.handlers_navegacion_extract import cambiar_pagina_extraccion
    
    rail = ft.NavigationRail(
            label_type=ft.NavigationRailLabelType.ALL,
            group_alignment=-0.9,
            on_change=lambda e: cambiar_pagina_extraccion(index=e.control.selected_index, page=page),
            height=250,
            width=80,
            destinations=[
                ft.FloatingActionButton(
                    icon=ft.Icons.DIFFERENCE,
                    tooltip="Convierte imágenes y PDFs en texto"
                ),
                ft.FloatingActionButton(
                    icon=ft.Icons.TRANSFORM,
                    tooltip="Extrae imagenes del PDFs"
                ),
                ft.FloatingActionButton(
                    icon=ft.Icons.PICTURE_AS_PDF,
                    tooltip="Extrae texto del PDFs"
                ),
            ],
        )
    return rail