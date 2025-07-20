from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pandas as pd

# Cargar el archivo Excel una sola vez al iniciar FastAPI
excel_path = "C:\Users\a0s10rw\Desktop\Backend_boda\invitacion_boda_Jessica_Alejandro\data\invitados.xlsx" 
df = pd.read_excel(excel_path)

# Filtrar filas con "Invitación dirigida a"
df = df[df["Invitación dirigida a"].notna()]

# Crear diccionario: { "Invitación dirigida a": Max Boletos }
boletos_dict = df.groupby("Invitación dirigida a")["Max Boletos"].max().to_dict()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def invitacion(request: Request):
    return templates.TemplateResponse("invitacion.html", {"request": request})

@app.post("/confirmar")
async def confirmar(nombre: str = Form(...), email: str = Form(...)):
    return HTMLResponse(content=f"<h2>¡Gracias por confirmar, {nombre}!</h2>")

@app.get("/", response_class=HTMLResponse)
async def invitacion(request: Request):
    return templates.TemplateResponse("invitacion.html", {
        "request": request,
        "boletos_dict": boletos_dict
    })
