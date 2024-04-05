"""A competition that occurs as part of a tournament."""
from format import Format
from gender import Gender
from level import Level


class Event:
    """
    A class to represent the competitive events that occur during a tournament.

    Attributes
    ----------
    format : Format
        An instance of the Format class that describes the format of the event.
    level : Level
        An instance of the Level class that describes the level of the event.
    gender : Gender
        An instance of the Gender class that describes what players can participate in an event.
    cost : float
        The cost to enter the event in USD.
    entries : int
        The number of entries for the event.

    Methods
    -------
    __str__():
        Print the event details.
    """

    def __init__(
        self, format: str, level: float, gender: str, cost: float, entries: int
    ):
        """
        Construct all the necessary attributes for the event object.

        Parameters
        ----------
        format : str
            The format of the event.
        level : float
            The level of the event.
        gender : str
            The gender(s) that can participate in the event.
        cost : float
            The cost to enter the event in USD.
        entries : int
            The number of entries for the event.

        Returns
        -------
        None
        """
        if not hasattr(Format, format):
            raise Exception
        self.format = Format[format]
        self.level = Level(level)
        if not hasattr(Gender, gender):
            raise Exception
        self.gender = Gender[gender]
        self.cost = cost
        self.entries = entries

    def __str__(self):
        """
        Print the event details.

        Returns
        -------
        str
            The event details.
        """
        description = (
            f"{self.level} {self.gender.value} {self.format.value} "
            f"(${self.cost}) {self.entries} entries"
        )

        return description
