import flet as ft
from assets.styles.styles import PADDING_TOP
from componentesUI.railExtraccionUI import railExtraccionPage

from utils.reconocimiento import extract_data_from_image, extract_text_from_pdf,extract_text_all_from_pdf
from utils.llm import llm_ordenar_texto, reformular_respuesta_send
from utils.dialog import opendialog
import pyperclip




def extractTextUI(page):
    
    titulo = ft.Text("Extraccion de PDF a Texto", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE)

    

    text = "Aqui estara su texto."
    
    
    respuesta_llm_view = ft.TextField(
        hint_text="Aqui estara su texto",
        autofocus=True,
        expand=True,
        multiline=True,
    )

    def vista_respuesta_view(text,page):


        respuesta_llm_view.value = text

        def copy_to_clipboard(text):
            pyperclip.copy(text)
            page.open(opendialog(page,"Copiado!","Texto copiado exitosamente"))

        return ft.Container(
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
            padding=ft.padding.all(30),
            border_radius=ft.border_radius.all(10),
            expand=True,
            
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        controls=[
                            ft.FloatingActionButton(
                                icon=ft.Icons.COPY,
                                on_click=lambda _: copy_to_clipboard(respuesta_llm_view.value),
                                tooltip="Copiar respuesta",
                                bgcolor=ft.Colors.TRANSPARENT
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                    
                    respuesta_llm_view,
                    
                ]
            )
        )

    async def on_file_upload(e):
        if e.files:
            file_path = e.files[0].path
            page.selected_file_path = file_path
            #print(file_path)
            if file_path.lower().endswith('.pdf'):
                text = extract_text_all_from_pdf(file_path)
                #respuesta_llm = await llm_ordenar_texto(text)
                #print(text)
                vista_respuesta_view(text,page)
                page.update()

            else:
                text="Por favor ingrese un archivo pdf valido!"
                vista_respuesta_view(text,page)
                page.update()
            
            page.update()

    

    file_picker = ft.FilePicker(on_result=on_file_upload)

    page.overlay.append(file_picker)



    def ui_extraccion_texto():
        return ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo,
                ft.IconButton(icon=ft.Icons.PICTURE_AS_PDF, on_click=lambda _: file_picker.pick_files()),
                vista_respuesta_view(text,page),
            ],
            
    )

    return ui_extraccion_texto()


def ExtractTextPlano(page):



    return ft.Container(
        padding=ft.padding.only(top=PADDING_TOP),
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    expand=False,
                    content=railExtraccionPage(page=page)
                ),
                ft.VerticalDivider(width=1),
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.top_center,
                    content=extractTextUI(page)
                ),
                
            ]
        )
    )