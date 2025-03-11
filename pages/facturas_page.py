"""
https://www.youtube.com/watch?v=_ieIlI_6xbQ&t=2267s
"""

import flet as ft

from componentesUI.railFacturas import railFacturas
from pages.extraccion_imagenes_pdf import PADDING_TOP

from utils.dialog import opendialog
from utils.exportacion import export_docx_to_pdf

"""
UTILS
"""

import flet as ft
import shutil
import zipfile
import os


#------------------


"""
UIX principal
"""

def input_factura_data(label,hint_text):

    return ft.TextField(
        label=label,
        hint_text=hint_text,
        # width=300,
        expand=True,
        
    )


def FacturasPageUI(page):

    titulo = ft.Text("Generar Factura", text_align=ft.TextAlign.CENTER,size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.ORANGE_400)
    #-----------------

    nombreempresatitulo = input_factura_data("Nombre Empresa","Nombre empresa")
    cifnif = input_factura_data("CIF/NIF", "CIF/NI")
    direccionfacturatitulo = input_factura_data("Direccion Factura", "Direccion Factura")

    # Facturar a
    nombre_facturar_a = input_factura_data("Nombre Empresa/Individuo","Nombre Empresa/Individuo")
    nif_facturar_a = input_factura_data("NIF", "NIF")
    direccion_facturar_a = input_factura_data("Direccion","Direccion")

    # Enviar a
    nombreenviara = input_factura_data("Nombre Destinatario","Nombre Destinatario")
    direccionenviara = input_factura_data("Direccion Destinatario","Direccion Destinatario")

    n_factura = input_factura_data("N° Factura", "N° Factura")
    fecha_factura = input_factura_data("Fecha factura","Fecha factura")
    n_pedido = input_factura_data("N° Pedido","N° Pedido")
    fecha_venc = input_factura_data("Fecha Vencimiento","Fecha Vencimiento")

    """
    DETALLE
    """
    descripcionproducto1 = input_factura_data("Descripcion Producto","Descripcion Producto")
    cant1 = input_factura_data("Cantidad producto","Cantidad producto")
    precio1 = input_factura_data("Precio","Precio")
    importe1 = input_factura_data("Importe","Importe")

    """
    UTILS
    """

    

    def generar_factura(datos):
        """
        Por ahora genera una factura en docx
        """
        try:
            

            shutil.copytree("./plantillas/plantilla","./plantillas/documento_tmp")
            with open("./plantillas/plantilla/word/document.xml", "r") as file:
                data = file.read()
                for key, value in datos.items():
                    data= data.replace(key,value)

            with open("./plantillas/documento_tmp/word/document.xml", "w") as file:
                file.write(data)
            
            with zipfile.ZipFile("./plantillas/factura_final.docx", 'w') as zipf:
                for root, dirs, files in os.walk("./plantillas/documento_tmp"):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), "./plantillas/documento_tmp"))

            shutil.rmtree("./plantillas/documento_tmp")
            export_docx_to_pdf("./plantillas/factura_final.docx", "./plantillas/factura_final.pdf")
            
            print("Factura generada")



        except Exception as e:
            print("error ", e)

    #--------------
    # HANDLERS
    def obtener_datos(e):
        #Faltan datos
        data_factura = {
            "nombreempresatitulo":nombreempresatitulo.value,
            "[CIF/NIF]":cifnif.value,
            "direccionfacturatitulo":direccionfacturatitulo.value,

        }
        generar_factura(data_factura)
    
















    #--------------

    def FacturaUI():
        return ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        titulo
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ResponsiveRow(
                    expand=True,
                    
                    controls=[
                        nombreempresatitulo,
                        cifnif,
                        direccionfacturatitulo
                    ],
                ),
            

                ft.Divider(),

                nombre_facturar_a,
                nif_facturar_a,
                direccion_facturar_a,

                ft.Divider(),

                nombreenviara,
                direccionenviara,

                ft.Divider(),

                n_factura,
                fecha_factura,
                n_pedido,
                fecha_venc,

                ft.Divider(),

                descripcionproducto1,
                cant1,
                precio1,
                importe1,

                ft.ElevatedButton(
                    "Generar Factura",
                    on_click=obtener_datos
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