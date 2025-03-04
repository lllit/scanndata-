import flet as ft
import json
import uuid
from datetime import date

from pages.send_email_page import SendEmailPage

from utils.reconocimiento import extract_data_from_image, extract_text_from_pdf
from utils.llm import llm_ordenar_texto, reformular_respuesta_send
from utils.send_email import send_email
from assets.styles.styles import PADDING_TOP
from utils.google_sheets_actions import GoogleSheet
from utils.dialog import opendialog


# -------------------------------
file_name_gs = "credencials/extdata-452119-f9321e8e1617.json"
google_sheet = "BD_ExtData"
sheet_name = "facturas_boletas"

def generate_uid():
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    return unique_id_str





# -------------------------------


def ExtractPage(page,cambiar_pagina):
    titulo = ft.Text("Lector IMG/PDF", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
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
                btn_email_icon.disabled = False
                btn_registrar_bd.disabled = False

                page.email_content = text_area.value
                

            except json.JSONDecodeError:
                
                
                text_area.value = "Error al procesar la respuesta del LLM"
                page.open(opendialog(page,"Error!","Error al procesar la respuesta"))

            #email_checkbox.disabled = False
            page.update()
    

    def on_send_email(e):
        send_email(subject_field.value, text_area.value, recipient_field.value,page.selected_file_path)
        page.open(opendialog(page,"Correo enviado!","El correo ha sido enviado exitosamente!"))

    def registrar_bd(e):

        uid = generate_uid()

        google = GoogleSheet(file_name_gs, google_sheet,sheet_name)

        current_date = date.today()

        value = [[
            uid,
            rut_emisor.value,
            razon_social_emisor.value,
            folio_dte.value,
            fecha.value,
            monto.value,
            primer_item.value,
            str(current_date)
        ]]

        range = google.get_last_row_range()
        google.write_data(range,value)
        page.open(opendialog(page,"Registro exitoso!", "Los datos han sido registrados en Google Sheets."))



    


    def go_to_send_email_page(e):
        # Mantener la barra de navegación y solo actualizar el contenido principal
        page.controls[1] = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: cambiar_pagina(1, page)
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



    file_picker = ft.FilePicker(on_result=on_file_upload)

    text_area = ft.TextField(value="", multiline=True, width=600, height=400, read_only=True, disabled=True)
    rut_emisor = ft.TextField(label="Rut Emisor", width=600, read_only=True)
    btn_email_icon = ft.IconButton(
                    icon=ft.Icons.EMAIL,
                    icon_color="blue400",
                    icon_size=30,
                    tooltip="Enviar por Gmail",
                    on_click=go_to_send_email_page,
                    disabled=True
                )

    razon_social_emisor = ft.TextField(label="Razon social Emisor", width=600, read_only=True)
    folio_dte = ft.TextField(label="Folio DTE", width=600, read_only=True)
    fecha = ft.TextField(label="Fecha", width=600, read_only=True)
    monto = ft.TextField(label="Monto", width=600, read_only=True)
    primer_item = ft.TextField(label="Primer Item", width=600, read_only=True)
    
    


    btn_send_gmail = ft.ElevatedButton("Enviar por Gmail", on_click=on_send_email, visible=False)
    subject_field = ft.TextField(label="Asunto", width=600, visible=False)
    recipient_field = ft.TextField(label="Destinatario", width=600, visible=False)
    
    btn_registrar_bd = ft.IconButton(
                    icon=ft.Icons.DATA_SAVER_ON,
                    icon_color=ft.Colors.GREEN_300,
                    icon_size=30,
                    tooltip="Registrar google sheets",
                    on_click=registrar_bd,
                    disabled=True
                )

    page.overlay.append(file_picker)


    ui_principal = ft.Column(
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
                    controls=[btn_email_icon,btn_registrar_bd,],
                    alignment=ft.MainAxisAlignment.END,
                ),
                padding=ft.padding.only(right=20)
            ),
            
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )


    return ft.Container(
        content=ft.Column(
                controls=[
                    ui_principal
                ]
            ),
        padding=ft.padding.only(top=PADDING_TOP)

    )

   