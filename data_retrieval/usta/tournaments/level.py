"""USTA-defined NTRP ratings used to group participants in tournament events."""
LEVELS = sorted(list(range(1, 8))[1:] + [x + 0.5 for x in range(1, 7)])


class Level:
    """
    A class to represent the level of a competitive event at a tournament.

    Attributes
    ----------
    value : float
        The event level. Levels span the range 1.5 to 7 in 0.5 point increments.

    Methods
    -------
    __str__():
        Prints the level.
    """

    def __init__(self, value: float):
        """
        Construct all the necessary attributes for the level object.

        Parameters
        ----------
        value : float
            The event level. Levels span the range 1.5 to 7 in 0.5 point increments.

        Returns
        -------
        None
        """
        if value not in LEVELS:
            raise Exception
        self.value = value

    def __str__(self):
        """
        Print the event level.

        Returns
        -------
        str
            The formatted string.
        """
        return f"{self.value}"
