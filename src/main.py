from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from src import models
from src.constants import IS_DEV
from src.database import engine
from src.logs import get_configured_logging
from src.routers import user

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url="/docs" if IS_DEV else None)

CORS_ALLOWED_ORIGINS = [  # location where your frontend is running
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

get_configured_logging()


@app.get("/")
def hello_world():
    return "hello world again"


@app.get("/is_dev")
def is_dev():
    logger.info("hello world")
    return IS_DEV


app.include_router(user.router)
