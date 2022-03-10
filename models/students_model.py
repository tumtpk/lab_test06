from pydantic import BaseModel

class Students(BaseModel):
    name: str
    description: str
    completed: bool
    date: str