import json
from typing import List

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

list_phone : List[PhoneModel] = []

def serialized_list_phone():
    converted_list = []
    for phone in list_phone:
        converted_list.append(phone.model_dump())
    return converted_list

@app.post("/phones")
def post_list_phone(new_phone_list: List[PhoneModel]):
    for new_phone in new_phone_list:
        list_phone.append(new_phone)
    return Response(content=json.dumps({"phones": serialized_list_phone()}),media_type="application/json",status_code=201)





