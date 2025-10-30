import os
import requests

LUMA_API_KEY = os.getenv("LUMA_API_KEY", "")


def create_job(prompt: str, clips: int = 3, aspect_ratio: str = "9:16") -> dict:
    """Crea un trabajo en Luma Dream Machine API.

    Esta funci\u00f3n es un placeholder y debe implementar la llamada real a la API de Luma.
    """
    # TODO: implementar llamada HTTP a Luma para crear un job
    return {"job_id": "placeholder-job-id"}


def get_job(job_id: str) -> dict:
    """Obtiene el estado de un trabajo en Luma.

    Devuelve un diccionario con el estado y el progreso.
    """
    # TODO: implementar consulta a Luma
    return {"status": "queued", "progress": 0.0}


def get_asset(asset_id: str) -> dict:
    """Obtiene la URL del asset en Luma.

    Devuelve un diccionario con la URL.
    """
    # TODO: implementar obtenci\u00f3n de asset en Luma
    return {"url": "https://example.com/video.mp4"}
