import flet as ft

from componentesUI.railExtraccionUI import railExtraccionPage

from utils.reconocimiento import extract_imagenes_pdf
from utils.dialog import opendialog
from assets.styles.styles import PADDING_TOP


def ExtractImgPage(page):
    titulo = ft.Text("Extraccion de imagenes en PDF", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_800)
    text_area = ft.TextField(value="", multiline=True, read_only=True, border=None, border_width=0)


    page.selected_file_path = None
    page.selected_save_path = None

    def on_file_upload(e):
        if e.files:
            file_path = e.files[0].path
            page.selected_file_path = file_path
            images = extract_imagenes_pdf(file_path)
            text_area.value = f"Se han extraído {len(images)} imágenes del PDF."
            save_btn.disabled = False
            page.update()

    def on_save_location_selected(e):
        if e.path:
            page.selected_save_path = e.path
            if page.selected_file_path:
                images = extract_imagenes_pdf(page.selected_file_path)
                for i, (image, ext) in enumerate(images):
                    image.save(f"{e.path}/image_{i+1}.{ext}")
                text_area.value = f"Imágenes guardadas en {e.path}."
                page.update()
                page.open(opendialog(page,
                                     "Imagenes exportadas exitosamente!",
                                     f"Imágenes guardadas en {e.path}.")
                )


    file_picker = ft.FilePicker(on_result=on_file_upload)
    save_picker = ft.FilePicker(on_result=on_save_location_selected)


    save_btn = ft.IconButton(
                    icon=ft.Icons.SAVE,
                    on_click=lambda _: save_picker.get_directory_path(),
                    tooltip="Seleccionar ubicación para guardar imágenes",
                    disabled=True
                )

    # Agregar los FilePickers a la página
    page.overlay.append(file_picker)
    page.overlay.append(save_picker)

    


    def ui_extraccion_img_pdf():
        return ft.Column(
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                titulo,
                ft.ElevatedButton("Seleccionar archivo PDF", on_click=lambda _: file_picker.pick_files()),
                text_area,
                save_btn
            ],
            
    )

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
                    content=ui_extraccion_img_pdf()
                ),
                
            ]
        )
    )