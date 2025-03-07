import uuid
import os




file_name_gs = os.environ.get("CREDENCIAL_SHEET")

google_sheet = ["BDExtDataFacturaBoleta","BDExtDataInventario"]


def generate_uid():
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    return unique_id_str