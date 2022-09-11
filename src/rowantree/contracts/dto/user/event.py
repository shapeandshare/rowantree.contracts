""" User Event Definition """

from typing import Optional, Union

from pydantic import BaseModel

from ...store_type import StoreType
from ...user_event_type_other import UserEventTypeOther


class UserEvent(BaseModel):
    """
    UserEvent DTO
    Defines an event of a user.
    In practice this is a state change for the user as a result of an in-world story or encounter.

    Attributes
    ----------
    title: str
        The title of the event.
    text: list[str]
        The optional list of text(s) of event.  The set of entries are ment to be rendered sequentially user-side.
    reward: Optional[dict[str, int]]
        The optional list of rewards (positive deltas to apply to the user)
    curse: Optional[dict[str, int]]
        The optional list of curses (negative deltas to apply to the user)
    """

    title: str
    text: dict[int, str]
    notification: dict[int, str]
    reward: dict[Union[UserEventTypeOther, StoreType], int]
    curse: dict[Union[UserEventTypeOther, StoreType], int]
