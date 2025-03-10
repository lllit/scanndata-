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

def show_delete_confirmation_dialog(page,on_confirm):
    def on_cancel(e):
        dialog.open = False
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirmación de eliminación"),
        content=ft.Text("¿Realmente quieres eliminar el producto?"),
        actions=[
            ft.TextButton("Cancelar", on_click=on_cancel),
            ft.TextButton("Eliminar", on_click=on_confirm),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.dialog = dialog
    dialog.open = True
    page.update()
    return dialog

