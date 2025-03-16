from assets.styles import css
import pdfkit
import pandas as pd



def config_invoice(nombre_destinatario,direccion_destinatario,telefono_destinatario,fecha_factura,numero_factura):
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Factura</title>
        <style>
        {css}
        </style>
    </head>
    <body>
        <header>
            <div class="container">
                <h1>Factura</h1>
            </div>
        </header>
        <div class="container">
            <div class="main">
                <h2>Detalles del Cliente</h2>
                <p>Nombre: {nombre_destinatario}</p>
                <p>Dirección: {direccion_destinatario}</p>
                <p>Teléfono: {telefono_destinatario}</p>
                <h2>Detalles de la Factura</h2>
                <p>Fecha: {fecha_factura}</p>
                <p>Número de Factura: {numero_factura}</p>
                <table>
                    <tr>
                        <th>Descripción</th>
                        <th>Cantidad</th>
                        <th>Precio Unitario</th>
                        <th>Total</th>
                    </tr>
                    <tr>
                        <td>Producto 1</td>
                        <td>2</td>
                        <td>$50.00</td>
                        <td>$100.00</td>
                    </tr>
                    <tr>
                        <td colspan="3" class="total">Subtotal</td>
                        <td>$235.00</td>
                    </tr>
                    <tr>
                        <td colspan="3" class="total">Impuesto (10%)</td>
                        <td>$23.50</td>
                    </tr>
                    <tr>
                        <td colspan="3" class="total"><strong>Total</strong></td>
                        <td><strong>$258.50</strong></td>
                    </tr>
                </table>
                <p>Gracias por su compra!</p>
            </div>
        </div>
    </body>
    </html>

    """
    return html

def create_invoice(html,invoice_number):
    pdf_file = f"temp/factura_{invoice_number}.pdf"
    options = {
        'enable-local-file-access': None
    }
    pdfkit.from_string(html,pdf_file,options=options)

def leer_archivo_csv():
    df = pd.read_csv("/temp/data.csv")
    data = df.to_dict('records')