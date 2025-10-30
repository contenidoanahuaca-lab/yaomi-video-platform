from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Yaomi Video Platform API",
    version="0.1.0",
    description="API para crear y gestionar proyectos de video IA por cr\u00e9ditos."
)

class JobRequest(BaseModel):
    prompt: str
    clips: int = 3
    aspect_ratio: str = "9:16"
    provider: str = "luma"

@app.post("/api/jobs")
async def create_job(req: JobRequest):
    """Crea un proyecto y trabajos en el proveedor de video IA.
    Esta implementaci\u00f3n es un placeholder y debe integrar la l\u00f3gica de cr\u00e9ditos y proveedor."""
    # TODO: validar saldo de cr\u00e9ditos y crear trabajos en proveedor
    return {"project_id": "placeholder-project-id", "jobs": ["job-id-1", "job-id-2"]}

@app.get("/api/jobs/{project_id}")
async def get_job_status(project_id: str):
    """Devuelve el estado del proyecto."""
    # TODO: obtener estado del proyecto (queued/processing/ready/failed) y progreso
    return {"project_id": project_id, "status": "queued", "progress": 0.0}

@app.get("/api/assets/{asset_id}")
async def get_asset(asset_id: str):
    """Devuelve una URL firmada para descargar el asset."""
    # TODO: devolver URL firmada del MP4 final o clip individual
    return {"asset_id": asset_id, "url": "https://example.com/asset.mp4"}

@app.post("/api/webhooks/luma")
async def webhook_luma(request: Request):
    """Procesa los eventos webhook enviados por Luma."""
    event = await request.json()
    # TODO: actualizar estados en base a event
    return {"received": True}

@app.post("/api/webhooks/stripe")
async def webhook_stripe(request: Request):
    """Procesa los eventos webhook de Stripe."""
    event = await request.json()
    # TODO: actualizar balance de cr\u00e9ditos en base a event
    return {"received": True}

@app.get("/health")
def health():
    """Endpoint de salud para Render."""
    return {"status": "ok"}
