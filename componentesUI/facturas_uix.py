import flet as ft


def input_factura_data(label,hint_text):

    # def textbox_changed(e):
    #     t.value = e.control.value
    #     page.update()

    return ft.TextField(
        label=label,
        hint_text=hint_text,
        # width=300,
        expand=True,
        border=ft.InputBorder.UNDERLINE,
        # on_change=textbox_changed
    )

def input_factura_number_data(label,hint_text):

    # def textbox_changed(e):
    #     t.value = e.control.value
    #     page.update()

    return ft.TextField(
        label=label,
        hint_text=hint_text,
        # width=300,
        expand=True,
        border=ft.InputBorder.UNDERLINE,
        input_filter=ft.NumbersOnlyInputFilter()
        # on_change=textbox_changed
    )

def formulario_resposive(form_iterable):
    return ft.ResponsiveRow(
    controls=[
        ft.Container(
            item, 
            col={"sm":12,"md":6,"lg":4}, 
            
        ) for item in form_iterable
    ],
    run_spacing=20,
    spacing=20
)
def formulario_resposive_4(form_iterable):
    return ft.ResponsiveRow(
    controls=[
        ft.Container(
            item, 
            col={"sm":12,"md":6,"lg":3}, 
            
        ) for item in form_iterable
    ],
    run_spacing=20,
    spacing=20
)
