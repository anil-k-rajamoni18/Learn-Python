from pydantic import BaseModel
from datetime import datetime


class Todo(BaseModel):
    id: int
    title: str
    status: str
    created_date: str = datetime.now().strftime('%Y-%m-%d')
    timestamp: datetime | None = datetime.now()


class Response(BaseModel):
    status: str
    status_code: int
    data: dict | list[dict] | str | None = None
    message: str | None = None
