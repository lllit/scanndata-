from utils.client import cliente_llm
from groq import APIStatusError
import json

cliente = cliente_llm()

async def llm_ordenar_texto(texto: str):
    system_message = """
        Recibirás texto de facturas o boletas. Tu objetivo es extraer la información relevante y devolverla en formato JSON **exclusivamente** con las siguientes claves:
        - Rut Emisor
        - Razon social Emisor
        - Folio DTE
        - Fecha
        - Total
        - Descripcion

        Asegúrate de que los valores estén completos y correctos. No agregues información extra ni omitas las claves.

        Siempre responde en español.
    """

    try:
        generated_message = cliente.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": texto}
            ],
            response_format={"type": "json_object"},
            model="llama3-8b-8192",
        )

        response = generated_message.choices[0].message.content
        #print("Respuesta JSON LLM:", response)

        return response
    


    except APIStatusError as e:
        if e.response.status_code == 413:
            return "El texto es demasiado grande."
        else:
            return f"Error en la API: {e}"
    except json.JSONDecodeError:
        return "Error al decodificar la respuesta JSON."
    except Exception as ex:
        return f"Error inesperado: {ex}"
        
async def reformular_respuesta_send(texto: str):
    system_message = """
        You will receive a text in json format, you have to create a text in human format, well written, 
        It has to be a formal email where you greet and then you say goodbye cordially, you have to send the information you receive in an orderly manner, it is only an informative email. 
        You are not representing the company, be aware that it is only an email to inform the data you are sending.

        You will always respond in Spanish
    """

    try:
        generated_message = cliente.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_message
                },
                {
                    "role": "user",
                    "content": texto,
                }
            ],
            model="llama3-8b-8192",
        )
        response = generated_message.choices[0].message.content
        #print("Respuesta send: ",response)
        return response
    except APIStatusError as e:
        if e.response.status_code == 413:
            return "El texto es demasiado grande"
        else:
            raise e
