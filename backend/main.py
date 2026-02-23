from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Messaging App API")

# Configuración de CORS para que React (puerto 3000) pueda conectarse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción cambiaremos esto por la IP de tu Oracle Cloud
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "API is working", "version": "1.0.0"}

@app.get("/messages")
async def get_messages():
    # Por ahora devolvemos datos "quemados" (mock data)
    return [
        {"id": 1, "user": "Julian", "content": "Hello from FastAPI!"},
        {"id": 2, "user": "System", "content": "Welcome back to your project."}
    ]
