import sys
import os

# Automatically add the current directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from app.routes import router as event_router

app = FastAPI()

app.include_router(event_router)
