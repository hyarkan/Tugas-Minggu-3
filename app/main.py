from fastapi import FastAPI
from app.routers.pmb import router as pmb_router

app = FastAPI(title="PMB API", version="1.0.0")
app.include_router(pmb_router)

@app.get("/")
def root():
    return {"message": "PMB API aktif"}
