from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ibm_assitant import crear_sesion, enviar_mensaje

app = FastAPI()#creamos la instancia de la aplicacion

class Message(BaseModel):
    msg: str
    user_id: str = "user_123" 

@app.post("/chat/")
def chat(data: Message):
    try:
        session_id = crear_sesion()
        resp = enviar_mensaje(session_id, data.msg, data.user_id)

        # Extraemos de forma segura el texto de la primera respuesta
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
