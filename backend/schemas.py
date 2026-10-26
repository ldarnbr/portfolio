from pydantic import BaseModel
from typing import List

class Project(BaseModel):
    id: int
    title: str
    tech: List[str]