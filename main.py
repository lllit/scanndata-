import flet as ft

from pages.home import HomePage
from handlers.handlers_navegacion import cambiar_pagina

from componentesUI.openmenu import create_navigation_drawer

from componentesUI.appbar import appbar_principal
from componentesUI.navbar import nav_bar

def main(page: ft.Page):
    page.title = "ScannData 0.1"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    



    drawer = create_navigation_drawer(page, cambiar_pagina)
    

    page.appbar = appbar_principal(page=page,drawer=drawer)


    # Configurar UI
    page.add(
        nav_bar(page)
    )

    
    page.add(
        HomePage(page)
    )


    page.update()




if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")