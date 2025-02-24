import flet as ft
from utils.send_email import send_email


def SendEmailPage(page):
    titulo = ft.Text("Enviar Correo", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    subject_field = ft.TextField(label="Asunto", width=600)
    recipient_field = ft.TextField(label="Destinatario", width=600)
    text_area = ft.TextField(value=page.email_content, multiline=True, width=600, height=400, read_only=True)
    
    def on_send_email(e):
        send_email(subject_field.value, text_area.value, recipient_field.value, page.selected_file_path)
        page.open(opendialog("Correo enviado!", "El correo ha sido enviado exitosamente!"))

    def opendialog(titulo_dialogo, content_dialogo):
        dlg = ft.AlertDialog(
            title=ft.Text(titulo_dialogo),
            content=ft.Text(content_dialogo),
            actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg))],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.update()
        return dlg


    

    return ft.Column(
        controls=[
            titulo,
            subject_field,
            recipient_field,
            text_area,
            ft.ElevatedButton("Enviar", on_click=on_send_email)
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )