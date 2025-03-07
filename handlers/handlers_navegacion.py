from pages.home import HomePage
from pages.extraccion_page import ExtractPage
from pages.extraccion_imagenes_pdf import ExtractImgPage
from pages.tables_view import TablesPage
from pages.calendario import CalendarPage




def cambiar_pagina(index, page):
    if index == 0:
        page.controls[1] = HomePage(page)
    elif index == 1:
        page.controls[1] = ExtractPage(page,cambiar_pagina)
    elif index == 2:
        page.controls[1] = TablesPage(page)
    elif index == 3:
        page.controls[1] = CalendarPage(page)
    page.update()


