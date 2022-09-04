from typing import Optional

from pydantic import BaseModel

from .state import UserState


class User(BaseModel):
    name: str
    state: Optional[UserState]
