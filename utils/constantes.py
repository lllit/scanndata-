import uuid
import os




file_name_gs = os.environ.get("CREDENCIAL_SHEET")

google_sheet = ["BD_ExtData","BD_ExtData2"]


def generate_uid():
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    return unique_id_str