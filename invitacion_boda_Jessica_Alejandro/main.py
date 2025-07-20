from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pandas as pd

excel_path = "data/invitados.xlsx"
df = pd.read_excel(excel_path)
df = df[df["Invitación dirigida a"].notna()]
boletos_dict = df.groupby("Invitación dirigida a")["Max Boletos"].max().to_dict()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def invitacion(request: Request):
    return templates.TemplateResponse("invitacion.html", {
        "request": request,
        "boletos_dict": boletos_dict
    })

@app.post("/confirmar")
async def confirmar(nombre: str = Form(...), email: str = Form(...)):
    return HTMLResponse(content=f"<h2>¡Gracias por confirmar, {nombre}!</h2>")
