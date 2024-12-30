from fastapi import APIRouter,Depends
from schemas import STask,STaskADD,STaskId
from typing import Annotated
from repository import TaskRepository


router = APIRouter(
    prefix="/tasks",
    tags=["Задачи"]
)

@router.post("")
async def add_task(
    task:Annotated[STaskADD,Depends()],

) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok":True , "task_id" : task_id}

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return {"tasks" : tasks}