""" UserIncomes Definition """

from pydantic import BaseModel

from ...store_type import StoreType
from .income import UserIncome


class UserIncomes(BaseModel):
    """
    UserIncomes DTO
    Defines a list of user incomes.
    """

    incomes: dict[StoreType, UserIncome]
