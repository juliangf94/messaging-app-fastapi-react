# 🚀 Messaging App - Diario de Desarrollo

## 📌 Estado Actual
- [x] Repositorio inicializado
- [x] Estructura de carpetas `backend/` y `frontend/`
- [ ] Conectar React con FastAPI (Siguiente paso)
- [ ] Base de Datos (Pendiente)

---

## 📅 Log de Pasos (Hoy: 23 de Febrero)

### Paso 1: El Backend (FastAPI)
* **¿Qué hice?**: Creé la carpeta `backend`, activé un entorno virtual e instalé FastAPI.
* **Archivo clave**: `backend/main.py`.
* **Comando para correrlo**: `uvicorn main:app --reload`.
* **Nota**: Agregué "CORS" para que el navegador no me bloquee cuando React intente hablar con FastAPI.
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```
-   `python3 -m venv venv`:
    +   Crea un Entorno Virtual (una carpeta llamada `venv`).
    +   Imagina que tienes otro proyecto que usa una versión vieja de FastAPI. 
    +   Si instalas todo de forma global en tu PC, se armaría un lío de versiones. 
    +   El entorno virtual crea una "burbuja" aislada donde solo instalas lo que este proyecto necesita.

-   `source venv/bin/activate`
    +   "Enciende" o activa la burbuja (el entorno virtual).
    +   Verás que en tu terminal aparece un (`venv`) al principio de la línea. 
    +   A partir de ahora, todo lo que instales se quedará guardado solo dentro de esa carpeta del proyecto.

-   `pip install fastapi uvicorn`
    +   Instala las dos herramientas base:
        *   **FastAPI**: El framework (el conjunto de herramientas) para construir las rutas de tu mensajería.
        *   **Uvicorn**: Es el motor (servidor ASGI) que hace que FastAPI pueda correr y escuchar peticiones en internet. Sin Uvicorn, FastAPI es solo código; con Uvicorn, es un servidor vivo.

### Paso 2: El Frontend (React + Vite)
* **¿Qué hice?**: Usé Vite para crear la base de React en la carpeta `frontend`.
* **Comando para correrlo**: `npm run dev`.
* **Diferencia con el stage de 2023**: Vite es mucho más rápido que `create-react-app`.
```Bash
cd ../frontend
npm create vite@latest . -- --template react
npm install
```


---

## 💡 Recordatorios Rápidos (Cheatsheet)
- **Puerto API**: http://127.0.0.1:8000
- **Documentación automática**: http://127.0.0.1:8000/docs (¡Swagger es genial para probar!)
- **Comando Git**: `git add . && git commit -m "mensaje"`

---

## 🛠️ Próximas Ideas / Por hacer
1. Hacer un `fetch()` en React para traer los mensajes.
2. Crear un formulario para enviar mensajes nuevos.
3. Meter Docker para que sea igualito al stage.
