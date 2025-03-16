import flet as ft

from pages.home import HomePage
from handlers.handlers_navegacion import cambiar_pagina

from componentesUI.openmenu import create_navigation_drawer
from componentesUI.appbar import appbar_principal
from componentesUI.navbar import nav_bar
from componentesUI.loadingUI import activity_indicator

def main(page: ft.Page):
    page.title = "ScannData 0.1"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    
    page.controls.append(activity_indicator)
    page.update()

    page.fonts = {
        "Roboto": "https://fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Mu4mxP.ttf",
        "RobotoBold": "https://fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlfBBc4.ttf",
        "RobotoItalic": "https://fonts.gstatic.com/s/roboto/v30/KFOkCnqEu92Fr1Mu51xIIzc.ttf"
    }

    page.theme = ft.Theme(
        font_family="Roboto"
    )


    drawer = create_navigation_drawer(page, cambiar_pagina)
    

    page.appbar = appbar_principal(page=page,drawer=drawer)

    page.controls.remove(activity_indicator)
    page.update()

    # Configurar UI
    page.add(
        nav_bar(page)
    )
    

    page.add(
        HomePage(page)
    )

    




if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")