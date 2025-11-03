from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Sebo Online API", version="1.0")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Testando API do SEBO ONLINE"}
