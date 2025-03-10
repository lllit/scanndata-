import flet as ft
from assets.styles.styles import colors
from componentesUI.loadingUI import activity_indicator
from utils.google_sheets_actions import GoogleSheet, GoogleSheetGeneral
from utils.constantes import file_name_gs, google_sheet
from utils.exportacion import PDF
from handlers.handlers_inventario import on_export_click_pdf,on_export_click_excel,on_save_location_selected_excel,on_save_location_selected_pdf
from utils.inventario_utils import edit_filed_text,show_data,update_data,add_data, on_delete_click,search_data
import pandas as pd


# MAIN DE PAGINA
def InventarioPage(page):

    page.controls.append(activity_indicator)
    page.update()
    
    page.title = "Inventario"

    global selected_row
    selected_row = None

    
    current_google_sheet = google_sheet[1]



    gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
    
    #---------------------------
    
    
    

    all_sheets = gs_general.get_all_sheets()
    
    
    #---------------------------
    current_sheet_name = all_sheets[0]
    # print(current_google_sheet)
    
    data = GoogleSheet(file_name_gs, current_google_sheet, current_sheet_name)
    #print(data.get_all_values())


    producto = ft.TextField(
        label="Nombre",
        border_color=ft.Colors.PURPLE_200
    )
    
    precio = ft.TextField(
        label="Precio",
        border_color=ft.Colors.PURPLE_200,
        input_filter=ft.NumbersOnlyInputFilter(),
        max_length=6
    )
    
    stock = ft.TextField(
        label="Stock",
        border_color=ft.Colors.PURPLE_200,
        input_filter=ft.NumbersOnlyInputFilter(),
        max_length=4
    )

    
    search_filed = ft.TextField(
        label="Buscar por nombre",
        suffix_icon=ft.Icons.SEARCH,
        border=ft.InputBorder.UNDERLINE,
        border_radius=ft.border_radius.all(10),
        border_color="white",
        label_style=ft.TextStyle(color="white"),
        on_change=lambda e: search_data(e,page,search_filed,datatable)
    )



    datatable = ft.DataTable(
        expand=True,
        border=ft.border.all(2,ft.Colors.PURPLE_200),
        data_row_color={
            ft.ControlState.SELECTED: "purple",
            ft.ControlState.PRESSED: "black"
        },
        border_radius=10,
        show_bottom_border=True,
        columns=[
            ft.DataColumn(
                ft.Text(producto.label, weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text(precio.label, weight=ft.FontWeight.BOLD)
            ),
            ft.DataColumn(
                ft.Text(stock.label,weight=ft.FontWeight.BOLD),
                numeric=True
            ),
        ]

    )
    

    form = ft.Container(
        bgcolor=colors[0],
        col=4,
        padding=ft.padding.all(10),
        expand=True,
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
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Ingrese sus datos", size=25, text_align=ft.TextAlign.CENTER),
                producto,
                precio,
                stock,
                ft.Container(
                    content=ft.Row(
                        wrap=True,
                        spacing=5,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.SAVE,
                                tooltip="Guardar",
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e: add_data(e,page,producto,precio,stock,datatable)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.UPDATE,
                                tooltip="Actualizar",
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e:update_data(e,page,producto,precio,stock,datatable)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                tooltip="Borrar",
                                icon_color=ft.Colors.WHITE,
                                on_click=lambda e: on_delete_click(e,page,datatable)
                            ),
                        ]
                    )
                )
            ]
        )
    )




    table = ft.Container(
        border_radius=ft.border_radius.only(bottom_left=10,bottom_right=10),
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
        col=8,
        expand=True,
        content=ft.Column(
            controls=[
                ft.Container(
                    padding=10,
                    content=ft.Row(
                        wrap=True,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            search_filed,
                            ft.IconButton(
                                icon=ft.Icons.EDIT,
                                tooltip="Editar",
                                icon_color="white",
                                on_click= lambda e:edit_filed_text(e,page,producto,precio,stock)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PICTURE_AS_PDF,
                                tooltip="Descargar en PDF",
                                icon_color="white",
                                on_click=lambda e: on_export_click_pdf(e,file_picker_pdf)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SAVE_ALT,
                                tooltip="Descargar en EXCEL",
                                icon_color="white",
                                on_click=lambda e:on_export_click_excel(e,file_picker_excel)
                            ),
                        ]
                    )
                ),
                ft.Column(
                    expand=True,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                datatable
                            ]
                        ),
                    ]
                )
            ]
            
        )
    )



    content = ft.ResponsiveRow(
        expand=True,
        controls=[
            form,
            table
        ]
    )

    
    
    
    
    
    
    
    file_picker_pdf = ft.FilePicker(on_result=lambda e: on_save_location_selected_pdf(e,page,data))
    file_picker_excel = ft.FilePicker(on_result=lambda e: on_save_location_selected_excel(e,page,data))
    page.overlay.append(file_picker_pdf)
    page.overlay.append(file_picker_excel)
    
    show_data(page=page,datatable=datatable)

    page.controls.remove(activity_indicator)
    page.update()

    return content