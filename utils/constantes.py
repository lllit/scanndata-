import uuid


file_name_gs = "credencials/extdata-452119-f9321e8e1617.json"
google_sheet = "BD_ExtData"
sheet_name = "facturas_boletas"

def generate_uid():
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    return unique_id_str