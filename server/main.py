import os
import time
import json
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, Body, Request


app = FastAPI()
router = APIRouter()


@router.post("/stat/{mac}")
async def create_entry(mac: str, request: Request):
    directory = 'out/'
    filename = f"inxi--{mac.replace(":","-")}--{int(time.time())}.json"
    content = await request.json()
    file_path = os.path.join(directory, filename)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, 'w') as file:
    #file.write(f"{content}")
        json.dump(content, file, indent=4)
    
app.include_router(router)
