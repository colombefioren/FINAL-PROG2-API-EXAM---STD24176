from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

@app.get("/ping")
def get_pong():
    return Response(content="pong", media_type="text/plain",status_code=200)

@app.get("/health")
def get_health():
    return Response(content="Ok",media_type="text/plain,status_code=200")

class Characteristic:
    ram_memory: int
    rom_memory: int

class PhoneModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic



