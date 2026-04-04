from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import document, ocr, vereification

app = FastAPI(title = "KYC V G13-M10 V0.9")
app.add_middleware(CORSMiddleware, 
                   allow_orgins=["hhtp://localhost:3000"],
                   allow_methods=["*"],
                   allow_headers = ["*"],
)

app.include_router(document.router,prefix="/api/v1")
app.include_router(ocr.router,prefix="/api/v1")
app.include_router(vereification.router,prefix="/api/v1")

@app.get("/health")
def health():
    return {"status":"ok"}
