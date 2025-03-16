"""
https://www.youtube.com/watch?v=_ieIlI_6xbQ&t=2267s
"""

import flet as ft
import pandas as pd

from fpdf import FPDF

from componentesUI.railFacturas import railFacturas
from pages.extraccion_imagenes_pdf import PADDING_TOP

from plantillas.factura import config_invoice, create_invoice
from utils.dialog import opendialog
from componentesUI.facturas_uix import input_factura_data,formulario_resposive,formulario_resposive_4
from handlers.handlers_facturas import obtener_datos,obtener_data_datos

from utils.exportacion import export_data_to_csv
from utils.generate_uid import generate_uid

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
        detalle_total.controls.extend(fila)
        productos.append(fila)
        #print(productos)
        page.update()

    def remove_producto(e):
        if productos:
            #print(productos)
            # Eliminar la última fila de productos
            fila = productos.pop()
            for control in fila:
                detalle_total.controls.remove(control)
                
            

            # Actualizar la página
            page.update()
        detalle_total
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

    def obtener_datos_input(e):
        resultados_titulo = []
        resultados_facturar_a = []
        resultados_enviar_a = []
        resultados_date = []


        for lista in formularios_titulo:
            resultados_titulo.append(lista.value)
        for lista in formularios_facturar_a:
            resultados_facturar_a.append(lista.value)
        for lista in formaulario_enviar_a:
            resultados_enviar_a.append(lista.value)
        for lista in formulario_date:
            resultados_date.append(lista.value)   
        
        all_result =  resultados_titulo + resultados_facturar_a +resultados_enviar_a+resultados_date

        nombre_empresa =all_result[0]
        cifnif_selected = all_result[1]
        direccion_factura = all_result[2]

        nombre_empresa_destinatario = all_result[3]
        nif_destinatario = all_result[4]
        direccion_empresa = all_result[5]

        nombre_persona_destinatario = all_result[6]
        direccion_destinatario = all_result[7]
        n_factura = all_result[8]
        fecha_factura_emision = all_result[9]
        n_pedido = all_result[10]


        

        # CREACION DEL PDF    
        pdf = FPDF()
        fontsize_titulo = 16
        fontsize_normal = 12

        pdf.add_page()
        logo_path = "assets/splash.jpg"
        pdf.image(name=logo_path, x=160, y=10, w=40, h=40)
        pdf.set_xy(10,10)
        pdf.set_font('Arial', size=fontsize_normal)
        pdf.cell(0,10,nombre_empresa, ln=True)
        pdf.cell(0,10,cifnif_selected, ln=True)
        pdf.cell(0,10,direccion_factura, ln=True)

        # pdf.cell(0,10,nif_destinatario, ln=True)
        # pdf.cell(0,10,fecha_factura_emision, ln=True)
        pdf.ln(20)

        # datos cliente
        pdf.set_font('Arial', size=fontsize_titulo)
        pdf.cell(0,10, txt="Factura", ln=True,align='C')
        pdf.set_font('Arial', size=fontsize_normal)
        pdf.cell(0,10,f"N° Factura: {n_factura}", ln=True,align='R')
        pdf.cell(0,10,f"Fecha Factura: {fecha_factura_emision}", ln=True,align='R')


        pdf.set_font('Arial', size=fontsize_titulo)
        pdf.cell(0,10,f"Datos del Cliente", ln=True)
        pdf.set_font('Arial', size=fontsize_normal)
        pdf.cell(0,10, f"Nombre Empresa/ Individuo: {nombre_empresa_destinatario}", ln=True)
        pdf.cell(0,10, f"NIF Empresa: {nif_destinatario}", ln=True)
        pdf.cell(0,10, f"Direccion Empresa: {direccion_empresa}", ln=True)

        pdf.cell(0,10, f"Nombre destinatario: {nombre_persona_destinatario}", ln=True)
        pdf.cell(0,10, f"Direccion destinatario: {direccion_destinatario}", ln=True)
        

        pdf.set_font('Arial', size=fontsize_titulo)
        pdf.cell(0,10,"Detalle de Factura", ln=True)

        pdf.set_font('Arial', size=fontsize_normal)

        # DETALLES DEL SERVICIO
        

        # Agregar productos dinámicamente
        productos_data = []
        data_total_dict = []
        

        for producto in detalle_total.controls:
            valores = producto.content.value.split('\n')
            productos_data.append(valores)
            
            
        
        print(productos_data)
        pdf.set_fill_color(200, 220, 255)
        pdf.cell(50,10, 'Detalle', border=1)
        pdf.cell(25,10, 'Cantidad', border=1)
        pdf.cell(20,10, 'Precio', border=1)
        pdf.cell(20,10, 'Importe', border=1, ln=True)
        for i in range(0, len(productos_data), 4):
            descripcion = productos_data[i][0]
            cantidad = productos_data[i+1][0]
            precio = productos_data[i+2][0]
            importe = productos_data[i+3][0]

            # DETALLES DEL SERVICIO
            

            pdf.cell(50, 10, descripcion, border=1)
            pdf.cell(25, 10, cantidad, border=1)
            pdf.cell(20, 10, precio, border=1)
            pdf.cell(20, 10, importe, border=1, ln=True)

            # Imprimir los valores asignados
            #print(f"Descripción: {descripcion}, Cantidad: {cantidad}, Precio: {precio}, Importe: {importe}")


        pdf_file = f"plantillas/temp/factura_{nombre_empresa}_{nombre_persona_destinatario}.pdf"
        pdf.output(pdf_file,'F')
        print("Factura generada")

        return all_result
        
            

    formulario_section1 = formulario_resposive(formularios_titulo)
    formulario_section2 = formulario_resposive(formularios_facturar_a)
    formulario_section3 = formulario_resposive(formaulario_enviar_a)
    formulario_section4 = formulario_resposive_4(formulario_date)
    


    detalle_total = formulario_resposive_4(descripcion_input)

    totales_section = formulario_resposive_4(totales_view)



    def FacturaUI():
        from datetime import datetime
        from dateutil.relativedelta import relativedelta
        fecha_hoy = datetime.now()
        fecha_formateada = fecha_hoy.strftime("%d-%m-%Y")

        fecha_sumada = fecha_hoy + relativedelta(months=2)
        fecha_sumada_formateada = fecha_sumada.strftime("%d-%m-%Y")

        nombreempresatitulo.value = "ScannData"
        cifnif.value = "00f/023d"
        direccionfacturatitulo.value = "Los Lagos"
        n_factura.value = "001"
        fecha_factura.value= fecha_formateada
        n_pedido.value = "001"
        fecha_venc.value = fecha_sumada_formateada



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
                detalle_total,
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
                                on_click=lambda e: obtener_datos_input(e),
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
                    #border_radius=ft.border_radius.all(30),
                    padding=ft.padding.all(10),
                    content=FacturasPageUI(page)
                )
            ]
        )
    )