
from pages.facturas_page import FacturasPage
from pages.facturas_edit import FacturasEditPage


def cambiar_pagina_factura(index, page):
    from handlers.handlers_navegacion_extract import cambiar_pagina_extraccion

    if index == 0:
        page.controls[1] = FacturasPage(page)
    elif index ==1:
        page.controls[1] = FacturasEditPage(page)
    page.update()