import flet as ft


def opendialog(page,titulo_dialogo, content_dialogo):
    dlg = ft.AlertDialog(
        title=ft.Text(titulo_dialogo),
        content=ft.Text(content_dialogo),
        actions=[ft.TextButton("OK", on_click=lambda e: page.close(dlg))],
        actions_alignment=ft.MainAxisAlignment.END,
    ) 
    page.update()
    return dlg