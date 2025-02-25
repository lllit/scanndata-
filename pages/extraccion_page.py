import flet as ft
import json
import os

from pages.send_email_page import SendEmailPage

from utils.reconocimiento import extract_data_from_image, extract_text_from_pdf
from utils.llm import llm_ordenar_texto, reformular_respuesta_send

from utils.send_email import send_email


# Obtener la ruta del ejecutable
# base_path = os.path.dirname(os.path.abspath(__file__))
# #tesseract_path = os.path.join(base_path, 'Tesseract-OCR', 'tesseract.exe')


def ExtractPage(page,cambiar_pagina):
    titulo = ft.Text("Extracción de data", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    texto_subid = ft.Text("Sube una imagen o un PDF:")


    # Variable para almacenar la ruta del archivo seleccionado
    page.selected_file_path = None

    page.email_content = ""

    async def on_file_upload(e):
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
                email_button.disabled = False
                
                page.email_content = text_area.value
                

            except json.JSONDecodeError:
                
                
                text_area.value = "Error al procesar la respuesta del LLM"
                page.open(opendialog("Error!","Error al procesar la respuesta"))

            #email_checkbox.disabled = False
            page.update()
    

    def on_send_email(e):
        send_email(subject_field.value, text_area.value, recipient_field.value,page.selected_file_path)
        page.open(opendialog("Correo enviado!","El correo ha sido enviado exitosamente!"))





    def opendialog(titulo_dialogo, content_dialogo):
        dlg = ft.AlertDialog(
            title=ft.Text(titulo_dialogo),
            content=ft.Text(content_dialogo),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg))],
            actions_alignment=ft.MainAxisAlignment.END,
        ) 
        page.update()
        return dlg


    def go_to_send_email_page(e):
        page.controls = page.controls[:2]
        
        # Crear el botón de volver
        back_button = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: cambiar_pagina(1)
        )
        # Agregar el botón de volver y la página de envío de correo
        page.add(
            ft.Row(
                controls=[back_button],
                alignment=ft.MainAxisAlignment.START
            )
        )
        page.controls[1].controls.clear()
        page.controls[1].controls.append(
            ft.Row(
                controls=[back_button],
                alignment=ft.MainAxisAlignment.START
            )
        )
        page.controls[1].controls.append(SendEmailPage(page))
        page.update()



    file_picker = ft.FilePicker(on_result=on_file_upload)

    text_area = ft.TextField(value="", multiline=True, width=600, height=400, read_only=True, disabled=True)
    rut_emisor = ft.TextField(label="Rut Emisor", width=600, read_only=True)
    email_button = ft.ElevatedButton("Enviar por Gmail", on_click=go_to_send_email_page, disabled=True)


    razon_social_emisor = ft.TextField(label="Razon social Emisor", width=600, read_only=True)
    folio_dte = ft.TextField(label="Folio DTE", width=600, read_only=True)
    fecha = ft.TextField(label="Fecha", width=600, read_only=True)
    monto = ft.TextField(label="Monto", width=600, read_only=True)
    primer_item = ft.TextField(label="Primer Item", width=600, read_only=True)
    
    


    btn_send_gmail = ft.ElevatedButton("Enviar por Gmail", on_click=on_send_email, visible=False)
    subject_field = ft.TextField(label="Asunto", width=600, visible=False)
    recipient_field = ft.TextField(label="Destinatario", width=600, visible=False)
    


    page.overlay.append(file_picker)

    return ft.Column(
        controls=[
            titulo,
            texto_subid,
            ft.ElevatedButton("Seleccionar archivo", on_click=lambda _: file_picker.pick_files()),
            
            rut_emisor,
            razon_social_emisor,
            folio_dte,
            fecha,
            monto,
            primer_item,

            subject_field,
            recipient_field,
            btn_send_gmail,
            ft.Container(
                content=ft.Row(
                    controls=[email_button],
                    alignment=ft.MainAxisAlignment.END,
                ),
                padding=ft.padding.only(right=20)
            ),
            
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )