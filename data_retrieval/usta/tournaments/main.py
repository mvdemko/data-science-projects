"""A script that retrieves USTA tournament data."""
from dates import Dates
from event import Event
from facility import Facility
from tournament import Tournament


def main():
    """
    Retrieve information on USTA tournaments.

    Returns
    -------
    None
    """
    # Example of creating a tournament
    f = Facility(
        name="La Jolla Tennis Club",
        address="7632 Draper Ave, La Jolla, CA, 92037",
        district="SAN_DIEGO",
        section="SOUTHERN_CALIFORNIA",
    )

    d = Dates("2024-04-13", "2024-04-14")

    e = [Event("DOUBLES", 4.5, "WOMEN", 30, 9), Event("DOUBLES", 4.5, "MIXED", 30, 6)]

    t = Tournament(
        name="Level 5 Open: SoCal NTRP Tour 750, La Jolla (Doubles)",
        category="ADULT",
        level=5,
        facility=f,
        status="OPEN",
        dates=d,
        events=e,
    )

    tournaments = [t]
    for ind, tourney in enumerate(tournaments):
        print(f"----- Tournament {ind+1} -----\n{tourney}")


if __name__ == "__main__":
    main()
