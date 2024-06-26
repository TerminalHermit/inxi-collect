import os
import time
import json
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, APIRouter, Body, Request
from fastapi.responses import FileResponse

app = FastAPI()
router = APIRouter()

directory = 'out/'

@router.get("/stat/{id}")
def get_file(id: str):
    file_path = os.path.join(directory, f"{id}")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404)
    return FileResponse(file_path, filename=f"{id}")

@router.post("/stat/{mac}")
async def create_entry(mac: str, request: Request):
    filename = f"inxi--{mac.replace(":","-")}--{int(time.time())}.json"
    content = await request.json()
    file_path = os.path.join(directory, filename)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, 'w') as file:
    #file.write(f"{content}")
        json.dump(content, file, indent=4)
    return filename
app.include_router(router)
