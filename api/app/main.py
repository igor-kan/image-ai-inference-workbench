from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response

from .processing import transform_image
from .runtime import runtime_status

app = FastAPI(title="Image AI Inference Workbench", version="0.1.0")


@app.get("/api/health")
def health() -> dict[str, object]:
    return {"ok": True, "service": "image-ai-workbench"}


@app.get("/api/runtime")
def runtime() -> dict[str, object]:
    return runtime_status()


@app.post("/api/transform")
async def transform(file: UploadFile = File(...)) -> Response:
    payload = await file.read()
    transformed = transform_image(payload)
    return Response(content=transformed, media_type="image/png")
