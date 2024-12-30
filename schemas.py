from pydantic import BaseModel
from typing import Annotated, Optional

class STaskADD(BaseModel):
    name:str
    description:Optional[str] = None
    
class STask(STaskADD):
    id:int

class STaskId(BaseModel):
    ok:bool = True
    task_id:int