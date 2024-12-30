from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
from typing import Annotated, Optional
from database import create_tables , delete_tables
from schemas import STask , STaskADD
from router import router as task_router

@asynccontextmanager
async def lifespan(app):
    await delete_tables()
    print("База очищена!")
    await create_tables()
    print("База готова!")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
