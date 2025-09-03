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
    return Response(content=json.dumps({"message": "The phone was created successfully"}),media_type="application/json",status_code=201)

@app.get("/phones")
def get_phone():
    return Response(content=json.dumps({"phones": serialized_list_phone()}),media_type="application/json",status_code=200)

@app.get("/phones/{id}")
def get_phone_by_id(id : str):
    for phone in list_phone:
        if phone.identifier == id:
            return Response(content=json.dumps(phone.model_dump()),media_type="application/json",status_code=200)
    return Response(content=json.dumps({"error":f"The phone of if {id} does not exist or was not found"}),media_type="application/json",status_code=404)

@app.put("/phones/{id}/characteristics")
def modify_phone_characteristics(id: str,new_characteristics: Characteristic):
    for phone in list_phone:
        if phone.identifier == id:
            phone.characteristics.ram_memory = new_characteristics.ram_memory
            phone.characteristics.rom_memory = new_characteristics.rom_memory
            return Response(content=json.dumps(phone.model_dump()),media_type="application/json",status_code=200)
    return Response(content=json.dumps({"error":f"The phone of if {id} does not exist or was not found"}),media_type="application/json",status_code=404)







