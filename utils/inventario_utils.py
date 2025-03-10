from utils.google_sheets_actions import GoogleSheet, GoogleSheetGeneral
from utils.constantes import file_name_gs, google_sheet
from utils.dialog import show_delete_confirmation_dialog
from utils.generate_uid import generate_uid
from utils.dialog import opendialog, show_delete_confirmation_dialog

import flet as ft


global selected_row
selected_row = None

current_google_sheet = google_sheet[1]
gs_general = GoogleSheetGeneral(file_name_gs, current_google_sheet)
all_sheets = gs_general.get_all_sheets()
current_sheet_name = all_sheets[0]

data = GoogleSheet(file_name_gs, current_google_sheet, current_sheet_name)

def clean_fileds(producto, precio, stock):
    producto.value = ""
    precio.value = ""
    stock.value = ""

def get_index(e,page):
    global selected_row

    if e.control.selected:
        e.control.selected = False
    else:
        e.control.selected  =True
    
    producto_name = e.control.cells[0].content.value
    print("Producto "+producto_name)
    
    for row in data.get_all_values():
        if row['Producto'] == producto_name:
            selected_row = row
            break
    print("Select row",selected_row)
    page.update()


def show_data(page,datatable):
    datatable.rows = []
    for x in data.get_all_values():
        datatable.rows.append(
            ft.DataRow(
                on_select_changed=lambda e: get_index(e,page=page),
                cells=[
                    ft.DataCell(ft.Text(x["Producto"])),
                    ft.DataCell(ft.Text(x["Precio"])),
                    ft.DataCell(ft.Text(x["Stock"])),
                ]
            )
        )
    page.update()

def add_data(e,page, producto, precio, stock,datatable):
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
            clean_fileds(producto,precio,stock)
            new_row = [[uid,name_producto,precio_producto,stock_producto]]
            
            last_row_range = data.get_last_row_range()
            #name_producto =selected_row["Producto"]

            data.write_data(last_row_range, new_row)
            page.open(opendialog(
                page=page,
                titulo_dialogo=f"Producto Agregado",
                content_dialogo="Producto Agregado exitosamente"
            ))
            show_data(page,datatable)
            clean_fileds(producto,precio,stock)
            page.update()

def update_data(e,page, producto, precio, stock,datatable):
    global selected_row

    name_producto = producto.value
    precio_producto = str(precio.value)
    stock_producto = str(stock.value)
    if len(name_producto) > 0 and len(precio_producto) >0 and len(stock_producto) > 0:
        clean_fileds(producto,precio,stock)
        uid = selected_row['uid']
        filtered_data = data.read_data_by_uid(uid)
        if not filtered_data.empty:
            values = [name_producto,precio_producto,stock_producto]
            data.write_data_by_uid(uid, values)
            name_producto =selected_row["Producto"]
            page.open(opendialog(
                page=page,
                titulo_dialogo=f"Producto Actualizado",
                content_dialogo=f"Producto {name_producto} Actualizado"
            ))
            show_data(page,datatable)
            clean_fileds(producto,precio,stock)
            page.update()

def delete_data(e,page,datatable):
    try:
        print(selected_row["uid"])
        uid_selected = selected_row["uid"]
        
        name_producto =selected_row["Producto"]
        data.delete_row_by_uid(uid_selected)
        page.open(opendialog(
            page=page,
            titulo_dialogo=f"Producto Eliminado",
            content_dialogo=f"Producto {name_producto} Eliminado"
        ))
        show_data(page,datatable)
        page.update()
    except Exception as e:
        print(e)

def on_delete_click(e, page, datatable):
    page.open(show_delete_confirmation_dialog(page, on_confirm=lambda _:delete_data(e,page,datatable)))



def edit_filed_text(e,page, producto, precio,stock):
    try:
        #print(selected_row)
        producto.value = selected_row['Producto']
        precio.value = selected_row['Precio']
        stock.value = selected_row['Stock']

        page.update()

    except Exception as e:
        print(e)


def search_data(e,page ,search_filed,datatable):
    search = search_filed.value.lower()
    producto_name = list(filter(lambda x: search in x['Producto'].lower(), data.get_all_values()))

    datatable.rows = []
    if search_filed.value !="":
        if len(producto_name) >0:
            for x in producto_name:
                datatable.rows.append(
                    ft.DataRow(
                        on_select_changed=lambda _: get_index(e,page),
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
        page.update()
        
    else:
        show_data(page,datatable)

    page.update()