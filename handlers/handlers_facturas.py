from utils.facturas_utils import generar_factura

def obtener_datos(e,
                  page,
                  factura_preview,
                  nombreempresatitulo,
                  cifnif,
                  direccionfacturatitulo
                ):
    #Faltan datos
    data_factura = {
        "nombreempresatitulo":nombreempresatitulo.value,
        "[CIF/NIF]":cifnif.value,
        "direccionfacturatitulo":direccionfacturatitulo.value,
        # faltan agregar datos
    }
    print(data_factura)
    #generar_factura(page,data_factura, factura_preview)
    
def obtener_data_datos(e,
                  page,
                  factura_preview,
                  data
                ):
    #Faltan datos
    
    print(data)
    #generar_factura(page,data_factura, factura_preview)
    
