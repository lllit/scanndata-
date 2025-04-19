import flet as ft
from datetime import date
import json

from assets.styles.styles import PADDING_TOP

from componentesUI.railExtraccionUI import railExtraccionPage

from utils.reconocimiento import extract_data_from_image, extract_text_from_pdf
from utils.llm import llm_ordenar_texto, reformular_respuesta_send
from utils.generate_uid import generate_uid
from utils.google_sheets_actions import GoogleSheet
from utils.dialog import opendialog
from utils.constantes import google_sheet

from handlers.handlers_go_send_email import go_to_send_email_page



file_name_gs = "credencials/extdata-452119-f9321e8e1617.json"
#google_sheet = "BD_ExtData"
sheet_name = "facturas_boletas"

def read_formulario_extract(label):
    return ft.TextField(
        label=label,
        width=600,
        read_only=True,
        border=ft.InputBorder.UNDERLINE
    )



def ExtractPageText(page, cambiar_pagina_extraccion):

    titulo = ft.Text("Lector Facturas/Boletas", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE)

    texto_subid = ft.Text("Sube una imagen o un PDF:")

    rut_emisor = read_formulario_extract(label="Rut Emisor")
    razon_social_emisor = read_formulario_extract(label="Razon social Emisor")
    folio_dte = read_formulario_extract(label="Folio DTE")
    fecha = read_formulario_extract(label="Fecha")
    monto = read_formulario_extract(label="Monto")
    primer_item = read_formulario_extract(label="Primer Item")

    text_area = ft.TextField(value="", multiline=True, width=600, height=400, read_only=True, disabled=True)
    
    btn_email_icon = ft.IconButton(
                    icon=ft.Icons.EMAIL,
                    icon_color="blue400",
                    icon_size=30,
                    tooltip="Enviar por Gmail",
                    on_click=lambda e: go_to_send_email_page(e,page,cambiar_pagina_extraccion),
                    disabled=True
                )

    btn_registrar_bd = ft.IconButton(
                    icon=ft.Icons.DATA_SAVER_ON,
                    icon_color=ft.Colors.GREEN_300,
                    icon_size=30,
                    tooltip="Registrar google sheets",
                    on_click=lambda e: registrar_bd(e),
                    disabled=True
                )


    def registrar_bd(e):

        uid = generate_uid()

        google = GoogleSheet(file_name_gs, google_sheet[0],sheet_name)

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
                
                #Ordenando la respuesta del llm en la UI
                
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

    file_picker = ft.FilePicker(on_result=on_file_upload)
    page.overlay.append(file_picker)

    return ft.Container(
        padding=ft.padding.only(top=PADDING_TOP,left=0,right=0,bottom=0),
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            spacing=0,
            controls=[
                # Rail
                ft.Container(
                    expand=False,
                    padding=0,
                    content=railExtraccionPage(page=page)
                ),
                ft.VerticalDivider(width=1),
                # Content
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.top_center,
                    padding=30,
                    gradient=ft.RadialGradient(
                        center=ft.Alignment(0,-1.25),
                        radius=1.4,
                        colors=[
                            "#424454",
                            "#393b52",
                            "#33354a",
                            "#2f3143",
                            "#292b3c",
                            "#222331",
                            "#1a1a25",
                            "#1a1b26",
                            "#21222f",
                            "#1d1e2a"
                        ],
                    ),
                    border_radius=ft.border_radius.all(20),
                    content=ft.Column(
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            titulo,
                            ft.Row(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    texto_subid,
                                    ft.IconButton(
                                        icon=ft.Icons.UPLOAD_FILE,
                                        tooltip="Seleccionar archivo", 
                                        on_click=lambda _: file_picker.pick_files()
                                    ),
                                ]
                            ),
                            ft.Column(
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                expand=True,
                                controls=[
                                    rut_emisor,
                                    razon_social_emisor,
                                    folio_dte,
                                    fecha,
                                    monto,
                                    primer_item,
                                    ft.Row(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            btn_email_icon,
                                            btn_registrar_bd
                                        ],
                                    ),
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )