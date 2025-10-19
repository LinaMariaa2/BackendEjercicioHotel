# BackendEjercicioHotel
Prueba de backend en FastApi e integracion de asistente watsonx

Comandos
para crear y activar el entorno venv
python -m venv venv
- cd venv
- cd Scripts 
- activate
cd .. ..

intalamos dependcias necesarias para crear la instancia y trabajar con fastApi
pip install fastapi uvicorn

Para ejecutar en FastApi 
utilizamos la libreria uvicorn
uvicorn main:app --reload (el reload es para que la ejecucion se mantenga y actulize cmabios)

las despendencias aqui se generan con 
pip freeze > requirements.txt
justo en un archivo requirements.txt que debemos de crear en la raiz del proyecto al principio


Aqui igual podemos manejar una arquitetucra mvc, pero por rapidez muchas veces no se realiza esa separacion.

despliegue en render https://backendejerciciohotel.onrender.com 

