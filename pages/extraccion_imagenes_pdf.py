import flet as ft

from utils.reconocimiento import extract_imagenes_pdf

def ExtractImgPage(page):
    titulo = ft.Text("Extraccion de imagenes en PDF", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    text_area = ft.TextField(value="", multiline=True, width=600, height=400, read_only=True)


    page.selected_file_path = None
    page.selected_save_path = None

    def on_file_upload(e):
        if e.files:
            file_path = e.files[0].path
            page.selected_file_path = file_path
            images = extract_imagenes_pdf(file_path)
            text_area.value = f"Se han extraído {len(images)} imágenes del PDF."
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
                page.open(dlg)


    file_picker = ft.FilePicker(on_result=on_file_upload)
    save_picker = ft.FilePicker(on_result=on_save_location_selected)

    # Agregar los FilePickers a la página
    page.overlay.append(file_picker)
    page.overlay.append(save_picker)

    # Crear el AlertDialog
    dlg = ft.AlertDialog(
        title=ft.Text("Guardado exitoso"),
        content=ft.Text("Las imágenes se han guardado correctamente."),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg))],
        actions_alignment=ft.MainAxisAlignment.END,
    )



    return ft.Column(
        controls=[
            titulo,
            ft.ElevatedButton("Seleccionar archivo PDF", on_click=lambda _: file_picker.pick_files()),
            ft.ElevatedButton("Seleccionar ubicación para guardar imágenes", on_click=lambda _: save_picker.get_directory_path()),
            text_area
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )