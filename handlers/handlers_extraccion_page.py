import flet as ft
import json
from pages.extraccion_page import text_area,rut_emisor,razon_social_emisor,folio_dte,fecha,monto,primer_item,btn_email_icon,btn_registrar_bd

from utils.reconocimiento import extract_data_from_image, extract_text_from_pdf
from utils.llm import llm_ordenar_texto, reformular_respuesta_send
from utils.dialog import opendialog



def file_picker(e,page):
    file_picker = ft.FilePicker(on_result=lambda e: on_file_upload(e,page))
    return file_picker


async def on_file_upload(e, page):
    if e.files:
        file_path = e.files[0].path
        page.selected_file_path = file_path



        if file_path.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
            respuesta_llm = await llm_ordenar_texto(text)
        else:
            text = extract_data_from_image(file_path)
            respuesta_llm = await llm_ordenar_texto(text)

        try:
            """
            Ordenando la respuesta del llm en la UI
            """
            text_area.value = await reformular_respuesta_send(respuesta_llm)

            data = json.loads(respuesta_llm)

            rut_emisor.value = data.get("Rut Emisor", "")
            razon_social_emisor.value = data.get("Razon social Emisor", "")
            folio_dte.value = data.get("Folio DTE", "")
            fecha.value = data.get("Fecha", "")
            monto.value = data.get("Total", "")
            primer_item.value = data.get("Primer Item", "")
            btn_email_icon.disabled = False
            btn_registrar_bd.disabled = False

            page.email_content = text_area.value


        except json.JSONDecodeError:


            text_area.value = "Error al procesar la respuesta del LLM"
            page.open(opendialog(page,"Error!","Error al procesar la respuesta"))

        #email_checkbox.disabled = False
        page.update()
    