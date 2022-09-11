""" UserMerchants Definition """

from pydantic import BaseModel

from ...store_type import StoreType
from ..merchant.merchant import Merchant


class UserMerchants(BaseModel):
    """
    UserMerchants DTO
    Defines a list of user merchants.
    """

    merchants: set[StoreType]
