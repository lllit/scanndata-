import flet as ft
from assets.styles.styles import colors
from pages.extraccion_page import generate_uid
from utils.google_sheets_actions import GoogleSheet, GoogleSheetGeneral
from utils.constantes import file_name_gs, google_sheet
from utils.exportacion import PDF

import pandas as pd


# MAIN DE PAGINA
def InventarioPage(page):

    page.title = "Inventario"

    global selected_row
    selected_row = None


    current_google_sheet = google_sheet[1]

    gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
    all_sheets = gs_general.get_all_sheets()
    
    current_sheet_name = all_sheets[0]
    # print(current_google_sheet)
    
    data = GoogleSheet(file_name_gs, current_google_sheet, current_sheet_name)
    #print(data.get_all_values())

    
    

    def show_data():
        datatable.rows = []
        for x in data.get_all_values():
            datatable.rows.append(
                ft.DataRow(
                    on_select_changed=get_index,
                    cells=[
                        ft.DataCell(ft.Text(x["Producto"])),
                        ft.DataCell(ft.Text(x["Precio"])),
                        ft.DataCell(ft.Text(x["Stock"])),
                    ]
                )
            )
        page.update()

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

    def search_data(e):
        search = search_filed.value.lower()
        producto_name = list(filter(lambda x: search in x['Producto'].lower(), data.get_all_values()))

        datatable.rows = []
        if search_filed.value !="":
            if len(producto_name) >0:
                for x in producto_name:
                    datatable.rows.append(
                        ft.DataRow(
                            on_select_changed=get_index,
                            cells=[
                                ft.DataCell(
                                    ft.Text(x['Producto'])
                                ),
                                ft.DataCell(
                                    ft.Text(x['Precio'])
                                ),
                                ft.DataCell(
                                    ft.Text(x['Stock'])
                                ),
                            ]
                        )
                    )
                page.update()
            
        else:
            show_data()
     
    
    search_filed = ft.TextField(
        label="Buscar por nombre",
        suffix_icon=ft.Icons.SEARCH,
        border=ft.InputBorder.UNDERLINE,
        border_radius=ft.border_radius.all(10),
        border_color="white",
        label_style=ft.TextStyle(color="white"),
        on_change=search_data
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

    def clean_fileds():
        producto.value = ""
        precio.value = ""
        stock.value = ""

    
    def add_data(e):
        name_producto = producto.value
        precio_producto = str(precio.value)
        stock_producto = str(stock.value)

        uid = generate_uid()


        if len(name_producto) > 0 and len(precio_producto) >0 and len(stock_producto) > 0:
            producto_exists = False
            for row in data.get_all_values():
                print(row["Producto"])
                if row["Producto"] == name_producto:
                    producto_exists = True
                    print("Producto ya existe")
                    break
            if not producto_exists:
                clean_fileds()
                new_row = [[uid,name_producto,precio_producto,stock_producto]]
                
                last_row_range = data.get_last_row_range()

                data.write_data(last_row_range, new_row)
                show_data()
                clean_fileds()
                page.update()

    def get_index(e):
        global selected_row

        if e.control.selected:
            e.control.selected = False
        else:
            e.control.selected  =True
        
        producto_name = e.control.cells[0].content.value
        #print(producto_name)
        
        for row in data.get_all_values():
            if row['Producto'] == producto_name:
                selected_row = row
                break
        #print(selected_row)
        page.update()

    def edit_filed_text(e):
        try:
            producto.value = selected_row['Producto']
            precio.value = selected_row['Precio']
            stock.value = selected_row['Stock']

            page.update()

        except Exception as e:
            print(e)


    def update_data(e):
        name_producto = producto.value
        precio_producto = str(precio.value)
        stock_producto = str(stock.value)

        if len(name_producto) > 0 and len(precio_producto) >0 and len(stock_producto) > 0:
            clean_fileds()
            uid = selected_row['uid']
            filtered_data = data.read_data_by_uid(uid)
            if not filtered_data.empty:
                values = [name_producto,precio_producto,stock_producto]
                data.write_data_by_uid(uid, values)
                show_data()
                clean_fileds()
                page.update()

    

    #------------------------------------------
    # Handlers Exportacion
    #------------------------------------------
    def on_save_location_selected_pdf(e):
        from datetime import datetime
        if e.path:
            folder_path = e.path
            print(folder_path)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"{folder_path}/db_inventario_{now}.pdf"
            #ave_pdf(path=file_path)

            pdf = PDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            column_widths = [40, 40, 40]
            header = ["Producto", "Precio", "Stock"]
            for i, col_name in enumerate(header):
                pdf.cell(column_widths[i], 10, col_name, 1, 0, "C")
            pdf.ln()
            data_ = data.get_all_values()
            for row in data_:
                pdf.cell(column_widths[0], 10, row["Producto"], 1)
                pdf.cell(column_widths[1], 10, str(row["Precio"]), 1)
                pdf.cell(column_widths[2], 10, str(row["Stock"]), 1)
                pdf.ln()

            # Save the PDF
            pdf.output(file_path)

            

            print("Guardado exitosamente")
            page.update()
    
    def on_save_location_selected_excel(e):
        from datetime import datetime
        if e.path:
            folder_path = e.path
            #print(folder_path)
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = f"{folder_path}/db_inventario_{now}.xlsx"

            data_ = data.get_all_values()

            df = pd.DataFrame(data_, columns=["Producto", "Precio", "Stock"])
            df.to_excel(file_path, index=False)

            

            print("Guardado exitosamente")
            page.update()


    
    def on_export_click_pdf(e):
        file_picker_pdf.get_directory_path()
        
    def on_export_click_excel(e):
        file_picker_excel.get_directory_path()
    #------------------------------------------
    #------------------------------------------

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
                                on_click=lambda e: add_data(e)
                            ),
                            ft.IconButton(
                                icon=ft.Icons.UPDATE,
                                tooltip="Actualizar",
                                icon_color=ft.Colors.WHITE,
                                on_click=update_data
                            ),
                            ft.IconButton(
                                icon=ft.Icons.DELETE,
                                tooltip="Borrar",
                                icon_color=ft.Colors.WHITE
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
                                on_click=edit_filed_text
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PICTURE_AS_PDF,
                                tooltip="Descargar en PDF",
                                icon_color="white",
                                on_click=on_export_click_pdf
                            ),
                            ft.IconButton(
                                icon=ft.Icons.SAVE_ALT,
                                tooltip="Descargar en EXCEL",
                                icon_color="white",
                                on_click=on_export_click_excel
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

    
    
    
    
    
    
    
    file_picker_pdf = ft.FilePicker(on_result=on_save_location_selected_pdf)
    file_picker_excel = ft.FilePicker(on_result=on_save_location_selected_excel)
    page.overlay.append(file_picker_pdf)
    page.overlay.append(file_picker_excel)
    
    show_data()

    return content