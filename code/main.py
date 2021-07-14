from fastapi import FastAPI
from time import sleep
import uvicorn
from datetime import datetime
import logging
from .data import *

logger = logging.getLogger()
app = FastAPI()

@app.get('/ping')
async def ping():
    return {"body": "healthy"}


@app.post('/invocations')
async def invocations():
    return {"body": "prediction"}

def compose_visibility():
    