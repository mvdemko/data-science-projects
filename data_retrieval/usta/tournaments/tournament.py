"""A tennis event sponsored by USTA."""
from category import Category
from dates import Dates
from event import Event
from facility import Facility
from status import Status


class Tournament:
    """
    A class to represent a tennis event sponsored by USTA.

    Attributes
    ----------
    name : str
        The name of the tournament.
    category : str
        The category of the tournament.
    level : int
        The level of the tournament. Level is a number between 1 and 7 that dictates how many
        points are awarded to participants.
    facility : Facility
        An instance of the Facility class that describes where the event will occur.
    status : str
        Describes whether the tournament is still accepting registrations.
    dates : Dates
        An instance of the Dates class that describes when the event will occur.
    events : list[Events]
        A list of Event instances that provide more details on the events that make up the
        tournament.

    Methods
    -------
    __str__():
        Print the tournament information.
    """

    def __init__(
        self,
        name: str,
        category: str,
        level: int,
        facility: Facility,
        status: str,
        dates: Dates,
        events: list[Event],
    ):
        """
        Construct all the necessary attributes for the tournament object.

        Attributes with a fixed set of possible values are converted to instances of the
        relevant class, which is a subclass of Enum. This includes category and status.

        Parameters
        ----------
        name : str
            The name of the tournament.
        category : str
            The category of the tournament.
        level : int
            The level of the tournament. Level is a number between 1 and 7 that dictates how many
            points are awarded to participants.
        facility : Facility
            An instance of the Facility class that describes where the event will occur.
        status : str
            Describes whether the tournament is still accepting registrations.
        dates : Dates
            An instance of the Dates class that describes when the event will occur.
        events : list[Events]
            A list of Event instances that provide more details on the events that make up the
            tournament.

        Returns
        -------
        None
        """
        self.name = name
        if not hasattr(Category, category):
            raise Exception
        self.category = Category[category]
        self.level = level
        self.facility = facility
        if not hasattr(Status, status):
            raise Exception
        self.status = Status[status]
        self.dates = dates
        self.events = events

    def __str__(self):
        """
        Print the tournament information.

        Returns
        -------
        str
            The formatted string.
        """
        description = (
            f"Name: {self.name}\n"
            f"Category: {self.category.value}\n"
            f"{self.facility}\n"
            f"Registration Status: {self.status.value}\n"
            f"Dates: {self.dates}\n"
            f"Events: "
        )

        for ind, event in enumerate(self.events):
            event_details = f"{event}"
            if ind < len(self.events) - 1:
                event_details += ", "
            description += event_details

        return description
