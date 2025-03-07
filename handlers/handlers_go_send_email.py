import flet as ft

from pages.send_email_page import SendEmailPage

def go_to_send_email_page(e, page,cambiar_pagina_extraccion):
    # Mantener la barra de navegación y solo actualizar el contenido principal
    page.controls[1] = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda e: cambiar_pagina_extraccion(0, page)
                    )
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            ft.Container(
                content=SendEmailPage(page),
                alignment=ft.alignment.center
            ),
            
        ]
    )
    page.update()

