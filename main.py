from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ibm_assitant import crear_sesion, enviar_mensaje

app = FastAPI()

# 🔹 Configurar CORS
origins = [
    "http://localhost:3000",  # tu frontend local de Next.js
    "https://tu-dominio-en-render.com",  # (opcional) tu dominio si ya lo despliegas
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],    # permite POST, GET, OPTIONS, etc.
    allow_headers=["*"],    # permite encabezados personalizados
)

# 🔹 Modelo
class Message(BaseModel):
    msg: str
    user_id: str = "user_123"

# 🔹 Ruta principal
@app.post("/chat/")
def chat(data: Message):
    try:
        session_id = crear_sesion()
        resp = enviar_mensaje(session_id, data.msg, data.user_id)

        output = resp.get("output", {})
        generic = output.get("generic", [])
        text = None
        if generic and generic[0].get("response_type") == "text":
            text = generic[0].get("text")

        return {
            "raw": resp,
            "text": text,
            "session_id": session_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
