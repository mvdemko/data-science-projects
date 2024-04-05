"""Categories used to group participants in a tournament."""
from enum import Enum


class Category(Enum):
    """
    A subclass of enumeration used to represent the competitive categories in a tournament event.

    Generally, participants fall into one of the four categories.
    """

    JUNIOR = "Junior (18 and under)"
    ADULT = "Adult (18+)"
    WHEELCHAIR = "Wheelchair (Junior and Adult)"
    WTN = "WTN Tournament"
