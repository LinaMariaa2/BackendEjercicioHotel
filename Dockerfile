# Imagen base ligera de Python
FROM python:3.11-slim


# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que usará FastAPI
EXPOSE 8000

# Comando para correr el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
