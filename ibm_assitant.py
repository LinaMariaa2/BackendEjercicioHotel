import os
from dotenv import load_dotenv
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Cargar variables del archivo .env
load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_URL = os.getenv("IBM_URL")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
ENVIRONMENT_ID = os.getenv("ENVIRONMENT_ID")  # ID de entorno (live o draft)

# Validar variables requeridas
if not all([IBM_API_KEY, IBM_URL, ASSISTANT_ID, ENVIRONMENT_ID]):
    raise RuntimeError("❌ Falta una variable de entorno. Revisa el archivo .env")

# Autenticador y cliente
authenticator = IAMAuthenticator(IBM_API_KEY)
assistant = AssistantV2(
    version="2023-10-01",
    authenticator=authenticator
)
assistant.set_service_url(IBM_URL)

def crear_sesion():
    """Crea una sesión en el assistant y devuelve el session_id"""
    resp = assistant.create_session(
        assistant_id=ASSISTANT_ID,
        environment_id=ENVIRONMENT_ID
    ).get_result()
    return resp["session_id"]

def enviar_mensaje(session_id, texto, user_id):
    """Envía un mensaje al assistant y devuelve la respuesta"""
    resp = assistant.message(
        assistant_id=ASSISTANT_ID,
        environment_id=ENVIRONMENT_ID,
        session_id=session_id,
        input={
            "message_type": "text",
            "text": texto,
            "options": {
                "return_context": True
            }
        },
        user_id=user_id   # ✅ Aquí se envía el ID obligatorio del usuario
    ).get_result()
    return resp
