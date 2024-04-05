"""The time period during which a tournament occurs."""
from datetime import date


class Dates:
    """
    A class to represent the time period spanned by a tournament.

    Attributes
    ----------
    start_date : datetime.date
        Start date of the event.
    end_date : datetime.date
        End date of the event.

    Methods
    -------
    __str__():
        Print the time period spanned by the event.
    """

    def __init__(self, start_date: str, end_date: str):
        """
        Construct all the necessary attributes for the dates object.

        Parameters
        ----------
        start_date : str
            Start date of the event in ISO format.
        end_date : str
            End date of the event in ISO format.

        Returns
        -------
        None
        """
        self.start_date = date.fromisoformat(start_date)
        if end_date < start_date:
            raise Exception
        self.end_date = date.fromisoformat(end_date)

    def __str__(self):
        """
        Print the time period spanned by the event.

        Returns
        -------
        str
            The formatted string.
        """
        return f"{self.start_date} through {self.end_date}"
