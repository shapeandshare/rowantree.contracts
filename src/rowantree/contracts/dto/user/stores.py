""" UserStores Definition """

from pydantic import BaseModel

from ...store_type import StoreType
from .store import UserStore


class UserStores(BaseModel):
    """
    UserStores DTO
    Defines a unique set of user stores.

    NOTE / TODO:
    This is a unique set of UserStore objects.

    Due to the legacy implementation this has been brought forward as-is.
    However,
    We want to make this a dictionary in the future given the access pattern (and uniqueness constraint) of the data.

    Attributes
    ----------
    stores: dict[StoreType, UserStore]
        A list of UserStore objects.
    """

    stores: dict[StoreType, UserStore]
