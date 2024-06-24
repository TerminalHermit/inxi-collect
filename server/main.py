import os
import time
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, APIRouter, Request


app = FastAPI()
router = APIRouter()


@router.post("/stat/")
async def create_entry(request: Request):
    directory = 'out/'
    filename = f"inxi-{int(time.time())}.json"
    content = await request.json()
    file_path = os.path.join(directory, filename)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(f"{content}")
    
app.include_router(router)
