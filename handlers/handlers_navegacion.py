from pages.facturas_page import FacturasPage
from pages.home import HomePage
from pages.extraccion_page import ExtractPage
from pages.tables_view import TablesPage
from pages.calendario import CalendarPage
from pages.inventario_page import InventarioPage

from componentesUI.loadingUI import activity_indicator

"""
Cambiar pagina del Navbar general
"""
def cambiar_pagina(index, page):
    if index == 0:
        page.controls[1] = HomePage(page)
    elif index == 1:
        page.controls[1] = ExtractPage(page)
    elif index == 2:
        page.controls[1] = InventarioPage(page)
    elif index == 3:
        page.controls[1] = FacturasPage(page)
    elif index == 4:
        page.controls[1] = TablesPage(page)
    elif index == 5:
        page.controls[1] = CalendarPage(page)
    page.update()


