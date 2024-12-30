from database import new_session,TaskOrm
from sqlalchemy import select
from main import STaskADD,STask

class TaskRepository:
    @classmethod
    async def add_one(cls, data:STaskADD):
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id



    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [STask.model_validate(task) for task in task_models]
            return task_schemas