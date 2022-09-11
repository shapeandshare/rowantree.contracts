""" Merchant Definition """
from pydantic import BaseModel

from ...store_type import StoreType


class Merchant(BaseModel):
    """
    Merchant DTO
    Defines the properties of a merchant.

    Attributes
    ----------
    name: StoreType
        The `StoreType`
    """

    name: StoreType
