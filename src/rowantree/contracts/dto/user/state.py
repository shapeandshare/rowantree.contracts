""" UserState Definition """

from pydantic import BaseModel

from ...feature_type import FeatureType
from ...store_type import StoreType
from ..merchant.merchant import Merchant
from .feature import UserFeature
from .income import UserIncome
from .notification import UserNotification
from .store import UserStore


class UserState(BaseModel):
    """
    UserState DTO
    Defines a user/player state.

    Attributes
    ----------
    active: bool
        Whether the user is active server side.
    stores: list[UserStore]
        A (unique) list of user stores. (see TODO)
    incomes: list[UserIncome]
        A (unique) list of user incomes. (see TODO)
    features: list[UserFeature]
        A (unique) list of user features. (see TODO)
    active_feature: UserFeature
        The current active user feature (location the user is currently in).
    population: int
        The size of the user population.
    merchants: list[Merchant]
        The (unique) list of user merchants. (see TODO)
    notifications: list[UserNotification]
        A list of most recent server events which occurred to the user.
    """

    active: bool
    stores: dict[StoreType, UserStore]
    incomes: dict[StoreType, UserIncome]
    features: dict[FeatureType, UserFeature]
    active_feature: FeatureType
    population: int
    merchants: set[StoreType]
    notifications: list[UserNotification]
