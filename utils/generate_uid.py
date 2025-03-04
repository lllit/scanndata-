import uuid

def generate_uid():
    unique_id = uuid.uuid4()
    unique_id_str = str(unique_id)
    return unique_id_str