import models
from constants import IS_DEV
from database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logs import get_configured_logging
from loguru import logger
from routers import item, items

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/docs" if IS_DEV else None)

CORS_ALLOWED_ORIGINS = [  # location where your frontend is running
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

get_configured_logging()


app.include_router(item.router)
app.include_router(items.router)
