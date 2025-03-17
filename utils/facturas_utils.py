import flet as ft
from utils.exportacion import pdf_to_image
from utils.dialog import opendialog
from fpdf import FPDF

"""
+--------------------------
|      CREACION DE PFD    |
+--------------------------
"""
class PDF(FPDF):
    def header(self):
        self.image("assets/splash.jpg", x=160, y=10, w=40, h=40)
        self.set_font('helvetica','B',20)

def generar_pdf(nombre_empresa,
                cifnif_selected,
                direccion_factura,
                n_factura,
                fecha_factura_emision,
                nombre_empresa_destinatario,
                nif_destinatario,
                direccion_empresa,
                nombre_persona_destinatario,
                direccion_destinatario,
                detalle_total,
                iva_view,
                totales_view,
                factura_preview
                ):
    """
    Funcion permite crear la factura con libreria FPDF
    """

    # CREACION DEL PDF    
    pdf = FPDF()
    fontsize_titulo = 16
    fontsize_normal = 12

    
    pdf.add_page()
    pdf.header()
    logo_path = "assets/splash.jpg"
    pdf.image(name=logo_path, x=160, y=10, w=40, h=40)
    pdf.set_xy(10,10)
    pdf.set_font('Arial', size=fontsize_normal)
    pdf.cell(0,10,nombre_empresa, ln=True)
    pdf.cell(0,10,cifnif_selected, ln=True)
    pdf.cell(0,10,direccion_factura, ln=True)

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
    

    for producto in detalle_total.controls:
        valores = producto.content.value.split('\n')
        productos_data.append(valores)
        
        
    
    print(productos_data)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(50,10, 'Detalle', border=1)
    pdf.cell(25,10, 'Cantidad', border=1)
    pdf.cell(30,10, 'Precio', border=1)
    pdf.cell(30,10, 'Importe', border=1, ln=True)
    
    subtotal_result=0
    total_iva_result=0
    for i in range(0, len(productos_data), 4):
        descripcion = productos_data[i][0]
        cantidad = productos_data[i+1][0]
        precio = productos_data[i+2][0]
        importe = productos_data[i+3][0]

        # DETALLES DEL SERVICIO
        

        pdf.cell(50, 10, descripcion, border=1)
        pdf.cell(25, 10, cantidad, border=1)
        pdf.cell(30, 10, f"${precio}", border=1)
        pdf.cell(30, 10, f"${importe}", border=1, ln=True)


        subtotal_result += (int(precio) * int(cantidad)) + int(importe)
        
        total_iva_result += (subtotal_result * iva_view.value)/100

        total_final_factura = subtotal_result + total_iva_result


        # Imprimir los valores asignados
        print(f"Descripción: {descripcion}, Cantidad: {cantidad}, Precio: {precio}, Importe: {importe}")

    
    
    # Actualizacion de datos en result
    totales_view[0].value = subtotal_result
    totales_view[2].value = total_iva_result
    totales_view[3].value = total_final_factura

    pdf.set_font('Arial', size=fontsize_titulo)
    pdf.cell(0,10,"Totales", ln=True)
    
    pdf.set_font('Arial', size=fontsize_normal)
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(50,10, 'Subtotal', border=1)
    pdf.cell(25,10, 'IVA', border=1)
    pdf.cell(35,10, 'Total IVA', border=1)
    pdf.cell(50,10, 'Total', border=1, ln=True)

    pdf.cell(50, 10, f"${str(subtotal_result)}", border=1)
    pdf.cell(25, 10, f"{str(iva_view.value)}%", border=1)
    pdf.cell(35, 10, f"${str(total_iva_result)}", border=1)
    pdf.cell(50, 10, f"${str(total_final_factura)}", border=1, ln=True)


    pdf_file = f"plantillas/temp/factura_{nombre_empresa}_{nombre_persona_destinatario}.pdf"
    pdf.output(pdf_file,'F')

    url_imagen = "./plantillas/factura_final_imagen.png"

    pdf_to_image(pdf_file,url_imagen)  

    factura_preview.src = url_imagen
    print("Factura generada")




"""
+--------------------------
|      OBTENER DATOS      |
+--------------------------
"""

def obtener_datos_input(e,
                        page,
                        formularios_titulo,
                        formularios_facturar_a,
                        formaulario_enviar_a,
                        formulario_date,
                        detalle_total,
                        iva_view,
                        totales_view,
                        factura_preview
                    ):
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


    generar_pdf(nombre_empresa,
                cifnif_selected,
                direccion_factura,
                n_factura,
                fecha_factura_emision,
                nombre_empresa_destinatario,
                nif_destinatario,
                direccion_empresa,
                nombre_persona_destinatario,
                direccion_destinatario,
                detalle_total,
                iva_view,
                totales_view,
                factura_preview
                )

    

    page.update()
    page.open(opendialog(page,"Factura generada","Proceso exisotoso"))
    return all_result
        
         