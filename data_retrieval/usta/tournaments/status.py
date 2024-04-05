"""The registration status of a tournament event."""
from enum import Enum


class Status(Enum):
    """
    A subclass of enumeration used to indicate the registration status of a tournament.

    Open means registrations are actively being accepted. Closed means it is no longer possible
    to register.
    """

    OPEN = "Open"
    CLOSED = "Closed"
