from datetime import datetime, timezone

from fastapi import FastAPI


app = FastAPI(title="Micro API de Gestão de Tarefas")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Retorna o estado de disponibilidade da API."""
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
