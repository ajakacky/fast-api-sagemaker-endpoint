from fastapi import FastAPI
from time import sleep
import uvicorn
from datetime import datetime

app = FastAPI()

@app.get('/ping')
async def ping():
    return {"message": "ok"}


@app.post('/invocations')
async def invocations():
    print(f"{datetime.now():%H:%M:%S} sleep start.")
    sleep(5)
    print(f"{datetime.now():%H:%M:%S} sleep end.")
    return {"message": "finish"}