import flet as ft
import json
import uuid
from datetime import date

from assets.styles.styles import colors


from utils.reconocimiento import extract_data_from_image, extract_text_from_pdf
from utils.llm import llm_ordenar_texto, reformular_respuesta_send
from utils.send_email import send_email
from utils.google_sheets_actions import GoogleSheet
from utils.dialog import opendialog
from utils.generate_uid import generate_uid

from assets.styles.styles import PADDING_TOP

from handlers.handlers_go_send_email import go_to_send_email_page


from componentesUI.railExtraccionUI import railExtraccionPage
from componentesUI.card_presentacion import card_presentacion
# -------------------------------
file_name_gs = "credencials/extdata-452119-f9321e8e1617.json"
google_sheet = "BD_ExtData"
sheet_name = "facturas_boletas"



# -------------------------------





def read_formulario_extract(label):
    return ft.TextField(
        label=label,
        width=600,
        read_only=True,
        border=ft.InputBorder.UNDERLINE
    )
   


def ExtractPage(page,cambiar_pagina):
    titulo = ft.Text("Funcionalidades de extracción", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_700)

    page.padding = 0



    ui_principal = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            titulo,
            ft.Row(
                wrap=True,
                controls=[
                    card_presentacion(
                        icon=ft.Icons.DIFFERENCE,
                        title="Boletas/Facturas",
                        subtitle="Convierte imágenes y PDFs en texto",
                    ),
                    card_presentacion(
                        icon=ft.Icons.DIFFERENCE,
                        title="PDF to png",
                        subtitle="Extraccion de imagenes de PDFs",
                    ),
                    
                ]
            ),
        ]
    )

    

    return ft.Container(
        padding=ft.padding.only(top=PADDING_TOP),
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(content=railExtraccionPage(page=page)),
                ft.VerticalDivider(width=1),
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.top_center,
                    content=ui_principal
                ),
            ],
            
        ),
        
    )

   