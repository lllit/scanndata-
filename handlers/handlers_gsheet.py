
from datetime import date

from utils.generate_uid import generate_uid
from utils.google_sheets_actions import GoogleSheet
from utils.dialog import opendialog

from pages.extraccion_page import rut_emisor,razon_social_emisor,folio_dte,fecha,monto,primer_item

#-----------------
file_name_gs = "credencials/extdata-452119-f9321e8e1617.json"
google_sheet = "BD_ExtData"
sheet_name = "facturas_boletas"
#-----------------

def registrar_bd(e, page):

    uid = generate_uid()

    google = GoogleSheet(file_name_gs, google_sheet,sheet_name)

    current_date = date.today()

    value = [[
        uid,
        rut_emisor.value,
        razon_social_emisor.value,
        folio_dte.value,
        fecha.value,
        monto.value,
        primer_item.value,
        str(current_date)
    ]]

    range = google.get_last_row_range()
    google.write_data(range,value)
    page.open(opendialog(page,"Registro exitoso!", "Los datos han sido registrados en Google Sheets."))