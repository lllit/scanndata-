import flet as ft


def railFacturas(page):

    from handlers.handlers_navegacion_facturas import cambiar_pagina_factura
    
    rail = ft.NavigationRail(
            label_type=ft.NavigationRailLabelType.ALL,
            group_alignment=-0.9,
            on_change=lambda e: cambiar_pagina_factura(index=e.control.selected_index, page=page),
            height=250,
            width=80,
            destinations=[
                ft.FloatingActionButton(
                    icon=ft.Icons.FACTORY,
                    tooltip="Generar Facturas"
                ),
                ft.FloatingActionButton(
                    icon=ft.Icons.MODE_EDIT_SHARP,
                    tooltip="Editar Facturas"
                ),
            ],
        )
    return rail