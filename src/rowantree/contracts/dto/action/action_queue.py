""" Command Queue Definition """
from pydantic import BaseModel

from .action import Action


class ActionQueue(BaseModel):
    """
    Command Queue DTO
    Used to hold a list of Actions (commands)

    Attributes
    ----------
    queue: list[Action]
        A list of Actions.
    """

    queue: list[Action]
