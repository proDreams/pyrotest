from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserSchemaInput(BaseModel):
    telegram_id: int


class UserSchemaOutput(UserSchemaInput):
    id: int
    created_at: datetime
    status_updated_at: datetime
    status: str
