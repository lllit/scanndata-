from pages.extraccion_page_texto import ExtractPageText
from pages.extraccion_imagenes_pdf import ExtractImgPage

def cambiar_pagina_extraccion(index, page):
    from handlers.handlers_navegacion_extract import cambiar_pagina_extraccion

    if index == 0:
        page.controls[1] = ExtractPageText(page, cambiar_pagina_extraccion)
    elif index ==1:
        page.controls[1] = ExtractImgPage(page)
    page.update()