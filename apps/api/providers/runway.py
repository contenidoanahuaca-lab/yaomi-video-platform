import os
import requests

RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY", "")


def create_job(prompt: str, clips: int = 3, aspect_ratio: str = "9:16") -> dict:
    """Crea un trabajo en Runway (placeholder).

    Esta implementaci\u00f3n es un stub; la integraci\u00f3n real se a\u00f1adir\u00e1 m\u00e1s adelante.
    """
    # TODO: implementar llamada HTTP a Runway para crear un job
    return {"job_id": "placeholder-runway-job"}


def get_job(job_id: str) -> dict:
    """Obtiene el estado de un trabajo en Runway (placeholder)."""
    # TODO: implementar consulta a Runway
    return {"status": "queued", "progress": 0.0}


def get_asset(asset_id: str) -> dict:
    """Obtiene la URL del asset en Runway (placeholder)."""
    # TODO: implementar obtenci\u00f3n de asset en Runway
    return {"url": "https://example.com/runway-video.mp4"}
