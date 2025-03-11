"""
https://www.youtube.com/watch?v=_ieIlI_6xbQ&t=2267s
"""

import flet as ft

from componentesUI.railFacturas import railFacturas
from pages.extraccion_imagenes_pdf import PADDING_TOP

from utils.dialog import opendialog
from componentesUI.facturas_uix import input_factura_data,formulario_resposive,formulario_resposive_4
from handlers.handlers_facturas import obtener_datos


#------------------



def FacturasPageUI(page):

    titulo = ft.Text("Generar Factura", text_align=ft.TextAlign.CENTER,size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_400)
    #-----------------
    
    titulo_emisor = ft.Text("Emisor:", weight=ft.FontWeight.BOLD, size=24)
    nombreempresatitulo = input_factura_data("Nombre Empresa","Nombre empresa")
    cifnif = input_factura_data("CIF/NIF", "CIF/NI")
    direccionfacturatitulo = input_factura_data("Direccion Factura", "Direccion Factura")

    titulo_facturar_a = ft.Text("Facturar a:", weight=ft.FontWeight.BOLD, size=24)
    # Facturar a
    nombre_facturar_a = input_factura_data("Nombre Empresa/Individuo","Nombre Empresa/Individuo")
    nif_facturar_a = input_factura_data("NIF", "NIF")
    direccion_facturar_a = input_factura_data("Direccion","Direccion")

    titulo_enviar_a = ft.Text("Enviar a:", weight=ft.FontWeight.BOLD, size=24)

    # Enviar a
    nombreenviara = input_factura_data("Nombre Destinatario","Nombre Destinatario")
    direccionenviara = input_factura_data("Direccion Destinatario","Direccion Destinatario")

    #--------------

    n_factura = input_factura_data("N° Factura", "N° Factura")
    
    fecha_factura = input_factura_data("Fecha factura","Fecha factura")
    n_pedido = input_factura_data("N° Pedido","N° Pedido")
    fecha_venc = input_factura_data("Fecha Vencimiento","12/12/2012")

    """
    DETALLE
    """
    titulo_detalle = ft.Text("Detalle:", weight=ft.FontWeight.BOLD, size=24)

    descripcionproducto1 = input_factura_data("Descripcion Producto","Descripcion Producto")
    cant1 = input_factura_data("Cantidad producto","Cantidad producto")
    precio1 = input_factura_data("Precio","Precio")
    importe1 = input_factura_data("Importe","Importe")

    
    """
    TOTALES VIEW
    """
    subtotal_view = input_factura_data("Subtotal","Subtotal")
    iva_view = input_factura_data("IVA", "IVA")
    total_iva_view = input_factura_data("Total IVA","Total IVA")
    total_view = input_factura_data("Total", "Total")


    #--------------------

    factura_preview = ft.Image(
        src="./assets/icon.png",
    )


    """
    UTILS
    """
    #######################
    #----------------
    # MEJORAR ESTO
    productos = []

    def add_producto(e):
        #print("Agregando producto")
        fila = [
            ft.Container(
                input_factura_data("Descripcion Producto","Descripcion Producto"),
                col={"sm": 12, "md": 6, "lg": 3}
            ),
            ft.Container(
                input_factura_data("Cantidad producto","Cantidad producto"),
                col={"sm": 12, "md": 6, "lg": 3}
            ),
            ft.Container(
                input_factura_data("Precio","Precio"),
                col={"sm": 12, "md": 6, "lg": 3}
            ),
            ft.Container(
                input_factura_data("Importe","Importe"),
                col={"sm": 12, "md": 6, "lg": 3}
            ),
        ]


        
        # Agregar los controles al ResponsiveRow
        productos_ui.controls.extend(fila)
        productos.append(fila)
        print(productos)
        page.update()

    def remove_producto(e):
        if productos:
            print(productos)
            # Eliminar la última fila de productos
            fila = productos.pop()
            for control in fila:
                productos_ui.controls.remove(control)
                
            

            # Actualizar la página
            page.update()
        productos_ui
        page.update()
    
    #----------------


    # add item
    add_item_btn = ft.FloatingActionButton(
        icon=ft.Icons.ADD, 
        on_click=lambda e: add_producto(e), 
    )
    remove_item_btn = ft.FloatingActionButton(
        icon=ft.Icons.REMOVE, 
        on_click=lambda e: remove_producto(e), 
    )
    #---------------------------
    formularios_titulo = [
        
        nombreempresatitulo,
        cifnif,
        direccionfacturatitulo,
    ]
    formularios_facturar_a =[
        nombre_facturar_a,
        nif_facturar_a,
        direccion_facturar_a,
    ]
    formaulario_enviar_a=[
        
        nombreenviara,
        direccionenviara,
    ]
    formulario_date=[
        n_factura,
        fecha_factura,
        n_pedido,
        fecha_venc,
    ]
    #------------------------

    descripcion_input = [
        descripcionproducto1,
        cant1,
        precio1,
        importe1
    ]

    totales_view = [
        subtotal_view,
        iva_view,
        total_iva_view,
        total_view
    ]

                

    formulario_section1 = formulario_resposive(formularios_titulo)
    formulario_section2 = formulario_resposive(formularios_facturar_a)
    formulario_section3 = formulario_resposive(formaulario_enviar_a)
    formulario_section4 = formulario_resposive_4(formulario_date)
    


    productos_ui = formulario_resposive_4(descripcion_input)

    totales_section = formulario_resposive_4(totales_view)



    def FacturaUI():
        n_pedido.value = 0

        return ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    controls=[
                        titulo
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                titulo_emisor,
                formulario_section1,
                titulo_facturar_a,
                formulario_section2,
                titulo_enviar_a,
                formulario_section3,
                ft.Divider(),
                ft.Container(
                    content=formulario_section4,
                    border=ft.border.all(1),
                    border_radius=ft.border_radius.all(10),
                    padding=ft.padding.all(10)
                ),
                ft.Divider(),
                titulo_detalle,
                productos_ui,
                ft.Row(
                    controls=[
                        add_item_btn,
                        remove_item_btn,
                    ],
                    alignment=ft.MainAxisAlignment.END
                    
                ),
                totales_section,
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                "Generar Factura",
                                on_click=lambda e: obtener_datos(e,page,factura_preview,nombreempresatitulo,cifnif,direccionfacturatitulo),
                            )
                        ],
                        spacing=30,
                        alignment=ft.MainAxisAlignment.END
                    ),
                    padding=ft.padding.only(top=30, bottom=30)
                ),
                ft.Container(
                    
                    content=ft.Row(
                        controls=[
                            factura_preview,
                            
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                )
            ]
        )
        

    return FacturaUI()
    












"""
MAIN de PAGINA
"""
def FacturasPage(page):
    return ft.Container(
        padding=ft.padding.only(top=PADDING_TOP),
        expand=True,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                ft.Container(
                    content=railFacturas(page)
                ),
                ft.Container(
                    expand=True,
                    alignment=ft.alignment.top_center,
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
                    border_radius=ft.border_radius.all(30),
                    padding=ft.padding.all(10),
                    content=FacturasPageUI(page)
                )
            ]
        )
    )